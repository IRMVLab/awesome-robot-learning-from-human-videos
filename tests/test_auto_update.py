"""Offline tests of evidence gates, incremental state, and README preservation."""

import argparse
import copy
import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("auto_update", ROOT / "scripts/auto_update.py")
au = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(au)
CONFIG = json.loads((ROOT / "config/auto-update.json").read_text())
WORKSPACE_README = (ROOT / "README.md").read_text()
# A stable fixture keeps daily tests independent of papers subsequently added by humans/bots.
README = """# Curated research

Intro, blogs, citation and table of contents must be preserved.

### Learning Paradigms

> Categories may overlap.

#### Agent+Human Data+Robot

> Agents that learn from human videos.

#### World Action Model (WAM)

#### 2026

- 🤖 [[arXiv 2026.08](https://arxiv.org/abs/2608.26103)] An Existing World Model [Code] [Page]

#### Vision-Language-Action Model (VLA)

#### 2026

- [[arXiv 2026.06](https://arxiv.org/abs/2606.14409)] An Existing VLA [Code] [Page]

#### In-Context & Video-Conditioned Learning (ICL & VCL)

#### 2026

- [[arXiv 2026.07](https://arxiv.org/abs/2607.15275)] An Existing Context Policy [Code] [Page]

---

### Information Transfer Taxonomy

#### Task-Oriented Transfer

- 🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.04600)] Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data [Code] [Page]

## Data Foundations

| Dataset | Size |
| --- | --- |
| Preserve this dataset | Unknown |
"""
HUMAN = "We learn transferable skills from egocentric human demonstration videos."
ROBOT = "We evaluate the resulting policy on a physical robot in the real world."
CATEGORY = "The agent uses human video demonstrations to plan and compose robot skills."
SOURCE = " ".join([HUMAN, ROBOT, CATEGORY])


def paper(aid="2610.12345", published="2026-10-15"):
    return {"id": aid, "version": 1, "title": "A Test Paper on Human Video Learning",
            "published": published, "updated": published + "T00:00:00Z", "abstract": HUMAN,
            "comments": "", "authors": ["Test Author"], "sources": ["arxiv_search"],
            "url": f"https://arxiv.org/abs/{aid}"}


def evidence():
    return {"source_text": SOURCE, "source_url": "https://arxiv.org/html/2610.12345v1",
            "source_urls": [], "truncated": False}


def assessment(categories=("agent",)):
    return {"decision": "include", "reason": "Human visual data is used for robot skills.",
            "human_data_quote": HUMAN, "robot_learning_quote": ROBOT,
            "categories": [{"id": cid, "confidence": .95, "quote": CATEGORY, "reason": "Supported by the method."} for cid in categories],
            "real_robot_quote": ROBOT, "code_url": None, "project_url": None}


def record(aid="2610.12345", published="2026-10-15", categories=("agent",)):
    return {"paper": paper(aid, published), "assessment": assessment(categories)}


class RenderingTests(unittest.TestCase):
    def test_noop_preserves_readme_exactly(self):
        self.assertEqual(au.render_readme(README, []), (README, []))
        self.assertEqual(au.render_readme(WORKSPACE_README, []), (WORKSPACE_README, []))

    def test_only_target_sections_change_and_existing_lines_survive(self):
        updated, additions = au.render_readme(README, [record(categories=tuple(au.HEADINGS))])
        self.assertEqual(len(additions), 4)
        self.assertEqual(updated.split(au.START)[0], README.split(au.START)[0])
        self.assertEqual(updated.split(au.END)[1], README.split(au.END)[1])
        for line in README.splitlines():
            if line.startswith("- "):
                self.assertIn(line + "\n", updated)

    def test_repeated_run_is_idempotent(self):
        records = [record(categories=("agent", "wam"))]
        once, _ = au.render_readme(README, records)
        twice, additions = au.render_readme(once, records)
        self.assertEqual(once, twice)
        self.assertEqual(additions, [])

    def test_existing_versioned_id_and_same_title_are_not_added_again(self):
        once, _ = au.render_readme(README, [record()])
        once = once.replace("/abs/2610.12345)", "/abs/2610.12345v2)")
        changed_title = record()
        changed_title["paper"]["title"] = "An Updated Title"
        self.assertEqual(au.render_readme(once, [changed_title])[1], [])
        # Also avoid duplicating the same title when its identifier differs.
        self.assertEqual(au.render_readme(once, [record("2610.99999")])[1], [])

    def test_cross_category_allowed_and_old_taxonomy_not_a_global_dedup(self):
        candidate = record("2602.04600", "2026-02-04", ("agent", "vla"))
        candidate["paper"]["title"] = "Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data"
        updated, additions = au.render_readme(README, [candidate])
        self.assertEqual(len(additions), 2)
        self.assertEqual(updated.split(au.END)[1], README.split(au.END)[1])

    def test_new_year_and_older_months(self):
        records = [record("2701.10001", "2027-01-02"), record("2601.10001", "2026-01-02"), record("2610.10001", "2026-10-02")]
        for r in records:
            r["paper"]["title"] += " " + r["paper"]["id"]
        updated, additions = au.render_readme(README, records)
        self.assertEqual(len(additions), 3)
        agent = updated.split("#### Agent+Human Data+Robot\n")[1].split("#### World Action Model")[0]
        self.assertLess(agent.index("#### 2027"), agent.index("#### 2026"))
        self.assertLess(agent.index("2610.10001"), agent.index("2601.10001"))
        self.assertIn("\n\n#### World Action Model", updated)

    def test_changed_layout_fails_closed(self):
        with self.assertRaises(ValueError):
            au.render_readme(README.replace(au.END, "\n### Moved taxonomy\n"), [record()])
        with self.assertRaises(ValueError):
            au.render_readme(README.replace("#### World Action Model (WAM)", "#### Renamed"), [record()])

    def test_untrusted_title_cannot_inject_markdown(self):
        p = paper()
        p["title"] = "A [false link](https://invalid.example)\n<script>alert(1)</script>"
        line = au.paper_line(p, assessment())
        self.assertNotIn("\n", line)
        self.assertNotIn("<script>", line)
        self.assertIn(r"\[false link\]", line)

    def test_badges_require_separate_evidence(self):
        a = assessment()
        a["real_robot_quote"] = ""
        a["code_url"] = "https://github.com/example/paper"
        self.assertNotIn("🌟", au.paper_line(paper(), a))
        self.assertNotIn("🤖", au.paper_line(paper(), a))
        self.assertIn("[Page]", au.paper_line(paper(), a))


class EvidenceTests(unittest.TestCase):
    def test_explicit_api_endpoint_accepts_http_custom_port_but_paper_links_do_not(self):
        endpoint = "http://43.133.198.249:3000/v1/chat/completions"
        self.assertEqual(au.public_url(endpoint, trusted_endpoint=True), endpoint)
        self.assertEqual(au.public_url("https://model.example.org:8443/v1", trusted_endpoint=True), "https://model.example.org:8443/v1")
        with self.assertRaises(ValueError):
            au.public_url(endpoint)
        with self.assertRaises(ValueError):
            au.public_url("https://model.example.org:8443/v1")
        for invalid in ("file:///tmp/key", "http://user:password@example.org/v1", "https://example.org:70000/v1"):
            with self.assertRaises(ValueError):
                au.public_url(invalid, trusted_endpoint=True)

    def test_model_request_reaches_transport_with_http_custom_port(self):
        network = au.Network()
        endpoint = "http://43.133.198.249:3000/v1/chat/completions"
        response = {"choices": [{"finish_reason": "stop", "message": {"content": json.dumps(assessment())}}]}
        with patch.dict(au.os.environ, {"LLM_BASE_URL": "http://43.133.198.249:3000/v1", "LLM_MODEL": "gpt-6-astra", "LLM_API_KEY": "dummy-key"}), \
             patch.object(network.opener, "open") as transport:
            transport.return_value.__enter__.return_value.read.return_value = json.dumps(response).encode()
            transport.return_value.__enter__.return_value.geturl.return_value = endpoint
            self.assertEqual(au.call_model(network, paper(), evidence(), CONFIG)["decision"], "include")
            request = transport.call_args.args[0]
            self.assertEqual(request.full_url, endpoint)
            self.assertEqual(request.get_header("Authorization"), "Bearer dummy-key")
            self.assertEqual(json.loads(request.data)["model"], "gpt-6-astra")

    def test_valid_quotes_and_multiple_categories(self):
        result = au.validate_assessment(assessment(("agent", "wam")), evidence(), CONFIG)
        self.assertEqual(result["decision"], "include")
        self.assertEqual(len(result["categories"]), 2)

    def test_fabricated_or_missing_quotes_require_review(self):
        for key in ("human_data_quote", "robot_learning_quote"):
            raw = assessment()
            raw[key] = "A fabricated quotation that never appeared in the paper."
            self.assertEqual(au.validate_assessment(raw, evidence(), CONFIG)["decision"], "review")

    def test_category_confidence_unknown_label_and_quote_are_checked(self):
        for change in ({"confidence": .7}, {"confidence": True}, {"confidence": float("nan")},
                       {"id": "datasets"}, {"quote": "Unsupported category quotation invented by a model."}):
            raw = assessment()
            raw["categories"][0].update(change)
            self.assertEqual(au.validate_assessment(raw, evidence(), CONFIG)["decision"], "review")

    def test_guessed_link_and_real_robot_claim_are_removed(self):
        raw = assessment()
        raw.update(code_url="https://github.com/guessed/repo", code_quote=CATEGORY,
                   real_robot_quote="Invented physical robot experiments that are not in the paper.")
        result = au.validate_assessment(raw, evidence(), CONFIG)
        self.assertIsNone(result["code_url"])
        self.assertEqual(result["real_robot_quote"], "")

    def test_link_requires_both_source_and_attribution(self):
        raw = assessment()
        raw.update(project_url="https://example.org/paper", project_quote=CATEGORY)
        ev = evidence()
        ev["source_urls"] = [raw["project_url"]]
        self.assertEqual(au.validate_assessment(raw, ev, CONFIG)["project_url"], raw["project_url"])
        raw["project_quote"] = ""
        self.assertIsNone(au.validate_assessment(raw, ev, CONFIG)["project_url"])

    def test_unreachable_links_and_readme_only_repos_get_no_star(self):
        class FakeNetwork:
            def get(self, *args, **kwargs):
                return b"ok", args[0]
            def json(self, *args, **kwargs):
                return {"tree": [{"type": "blob", "path": "README.md"}]}
        raw = assessment()
        raw["code_url"] = "https://github.com/example/paper"
        au.verify_links(FakeNetwork(), raw, [])
        self.assertFalse(raw["public_code"])
        with patch.object(FakeNetwork, "get", side_effect=OSError("offline")):
            au.verify_links(FakeNetwork(), raw, [])
        self.assertIsNone(raw["code_url"])

    def test_network_blocks_local_addresses_and_credential_redirects(self):
        with patch.object(au.socket, "getaddrinfo", return_value=[(2, 1, 6, "", ("127.0.0.1", 443))]):
            with self.assertRaises(ValueError):
                au.public_url("https://localhost/private")
        request = au.Request("https://api.example.org/v1/chat/completions", headers={"Authorization": "Bearer test"})
        with patch.object(au, "public_url", return_value="https://other.example.org/"):
            with self.assertRaises(ValueError):
                au.SafeRedirect().redirect_request(request, None, 302, "redirect", {}, "https://other.example.org/")


class SourceTests(unittest.TestCase):
    def test_trending_source_does_not_fill_queue_with_unrelated_papers(self):
        candidate = paper()
        candidate["abstract"] = HUMAN + " " + ROBOT
        self.assertTrue(au.hf_candidate(candidate))
        unrelated = paper()
        unrelated.update(title="A New Language Model", abstract="We train a language model on human text.")
        self.assertFalse(au.hf_candidate(unrelated))

    def test_atom_metadata_and_versions(self):
        xml = b'''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/" xmlns:x="http://arxiv.org/schemas/atom">
        <o:totalResults>1</o:totalResults><entry><id>http://arxiv.org/abs/2610.12345v2</id>
        <title> A\n Real Title </title><published>2026-10-01T00:00:00Z</published><updated>2026-10-10T00:00:00Z</updated>
        <summary>An abstract.</summary><author><name>An Author</name></author><x:comment>Project: https://example.org/</x:comment></entry></feed>'''
        papers, total = au.parse_atom(xml)
        self.assertEqual(total, 1)
        self.assertEqual(papers[0]["id"], "2610.12345")
        self.assertEqual(papers[0]["version"], 2)
        self.assertEqual(papers[0]["published"], "2026-10-01")
        self.assertEqual(papers[0]["title"], "A Real Title")

    def test_missed_run_recovery_and_cap(self):
        today = dt.date(2026, 10, 21)
        self.assertEqual(au.search_start(CONFIG, {}, today, None), dt.date(2026, 10, 14))
        self.assertEqual(au.search_start(CONFIG, {"last_search_date": "2026-10-01"}, today, None), dt.date(2026, 9, 30))
        self.assertEqual(au.search_start(CONFIG, {"last_search_date": "2025-01-01"}, today, None), today - dt.timedelta(days=90))

    def test_overflow_does_not_silently_lose_results(self):
        class FakeNetwork:
            def get(self, *args, **kwargs):
                return b'<feed xmlns:o="http://a9.com/-/spec/opensearch/1.1/"><o:totalResults>301</o:totalResults></feed>', args[0]
        with self.assertRaisesRegex(RuntimeError, "above cap"):
            au.discover(FakeNetwork(), CONFIG, dt.date(2026, 10, 1), dt.date(2026, 10, 21), [])


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "README.md").write_text(README)
        (self.root / "data/auto-update").mkdir(parents=True)
        self.state_path = self.root / "data/auto-update/state.json"
        self.initial_state = '{"schema_version":1,"papers":{}}\n'
        self.state_path.write_text(self.initial_state)
        self.config_path = self.root / "config.json"
        self.config_path.write_text(json.dumps(CONFIG))
        self.args = argparse.Namespace(root=self.root, config=self.config_path, lookback_days=7,
                                       dry_run=False, discover_only=False, report=self.root / "report.md", result=self.root / "result.json")
        env = patch.dict(au.os.environ, {"LLM_API_KEY": "test-not-a-real-key", "LLM_BASE_URL": "https://model.example.org/v1", "LLM_MODEL": "test-model"})
        env.start()
        self.addCleanup(env.stop)

    def execute(self, found=None, model=None):
        found = found if found is not None else {"2610.12345": paper()}
        with patch.object(au, "discover", return_value=copy.deepcopy(found)), \
             patch.object(au, "fetch_evidence", return_value=evidence()), \
             patch.object(au, "call_model", return_value=model or assessment()) as call, \
             patch.object(au, "verify_links"):
            self.assertEqual(au.run(self.args), 0)
            return call.call_count

    def test_dry_run_has_no_repository_writes(self):
        self.args.dry_run = True
        self.assertEqual(self.execute(), 1)
        self.assertEqual((self.root / "README.md").read_text(), README)
        self.assertEqual(self.state_path.read_text(), self.initial_state)
        self.assertEqual(len(json.loads(self.args.result.read_text())["additions"]), 1)

    def test_success_persists_cache_and_second_run_skips_model(self):
        self.assertEqual(self.execute(), 1)
        once = (self.root / "README.md").read_text()
        self.assertEqual(self.execute(), 0)
        self.assertEqual((self.root / "README.md").read_text(), once)
        self.assertEqual(json.loads(self.state_path.read_text())["papers"]["2610.12345"]["status"], "accepted")

    def test_rejection_is_cached_and_does_not_edit_readme(self):
        self.execute(model={"decision": "exclude", "reason": "Uses only robot demonstrations."})
        self.assertEqual(self.execute(), 0)
        self.assertEqual((self.root / "README.md").read_text(), README)

    def test_excluded_paper_is_not_sent_to_model(self):
        config = copy.deepcopy(CONFIG)
        config["excluded_arxiv_ids"] = ["2610.12345"]
        self.config_path.write_text(json.dumps(config))
        self.assertEqual(self.execute(), 0)

    def test_pending_queue_survives_batch_limit(self):
        config = copy.deepcopy(CONFIG)
        config["max_candidates_per_run"] = 1
        self.config_path.write_text(json.dumps(config))
        found = {"2610.12345": paper(), "2610.12346": paper("2610.12346")}
        self.assertEqual(self.execute(found), 1)
        state = json.loads(self.state_path.read_text())
        self.assertEqual(sum(r["status"] == "pending" for r in state["papers"].values()), 1)
        self.assertEqual(self.execute({}), 1)

    def test_model_auth_failure_leaves_files_untouched(self):
        with patch.object(au, "discover", return_value={"2610.12345": paper()}), \
             patch.object(au, "fetch_evidence", return_value=evidence()), \
             patch.object(au, "call_model", side_effect=RuntimeError("Model API HTTP 401")):
            with self.assertRaises(RuntimeError):
                au.run(self.args)
        self.assertEqual((self.root / "README.md").read_text(), README)
        self.assertEqual(self.state_path.read_text(), self.initial_state)

    def test_invalid_api_config_fails_before_discovery(self):
        with patch.dict(au.os.environ, {"LLM_BASE_URL": "43.133.198.249:3000/v1"}), \
             patch.object(au, "discover") as discover:
            with self.assertRaisesRegex(ValueError, "LLM_BASE_URL"):
                au.run(self.args)
            discover.assert_not_called()

    def test_all_model_errors_fail_run_keep_files_and_preserve_safe_diagnostics(self):
        with patch.object(au, "discover", return_value={"2610.12345": paper()}), \
             patch.object(au, "fetch_evidence", return_value=evidence()), \
             patch.object(au, "call_model", side_effect=ValueError("Model output truncated; test-not-a-real-key")):
            self.assertEqual(au.run(self.args), 1)
        self.assertEqual((self.root / "README.md").read_text(), README)
        self.assertEqual(self.state_path.read_text(), self.initial_state)
        report = self.args.report.read_text()
        result = json.loads(self.args.result.read_text())
        self.assertTrue(result["failed"])
        self.assertIn("Model output truncated", report)
        self.assertNotIn("test-not-a-real-key", report + self.args.result.read_text())
        self.assertIn("[REDACTED]", result["model_errors"][0]["error"])

    def test_partial_model_failure_can_preserve_verified_additions(self):
        found = {"2610.12345": paper(), "2610.12346": paper("2610.12346")}
        with patch.object(au, "discover", return_value=found), \
             patch.object(au, "fetch_evidence", return_value=evidence()), \
             patch.object(au, "call_model", side_effect=[assessment(), ValueError("Missing decision or reason")]), \
             patch.object(au, "verify_links"):
            self.assertEqual(au.run(self.args), 0)
        result = json.loads(self.args.result.read_text())
        self.assertFalse(result["failed"])
        self.assertEqual(len(result["model_errors"]), 1)
        self.assertEqual(len(result["additions"]), 1)
        state = json.loads(self.state_path.read_text())["papers"]
        self.assertEqual(state["2610.12345"]["status"], "accepted")
        self.assertEqual(state["2610.12346"]["status"], "retry")

    def test_endpoint_change_retries_cached_decisions(self):
        self.execute(model={"decision": "exclude", "reason": "Test rejection"})
        with patch.dict(au.os.environ, {"LLM_BASE_URL": "http://43.133.198.249:3000/v1"}):
            self.assertEqual(self.execute(), 1)

    def test_missing_full_text_is_retried_then_requires_review(self):
        with patch.object(au, "discover", return_value={"2610.12345": paper()}), \
             patch.object(au, "fetch_evidence", side_effect=ValueError("PDF unavailable")), \
             patch.object(au, "call_model") as call:
            for _ in range(4):
                au.run(self.args)
            call.assert_not_called()
        stored = json.loads(self.state_path.read_text())["papers"]["2610.12345"]
        self.assertEqual(stored["status"], "review")
        self.assertEqual(stored["attempts"], 3)
        self.assertEqual((self.root / "README.md").read_text(), README)

    def test_discovery_only_needs_no_credentials_and_does_not_write_state(self):
        self.args.discover_only = True
        with patch.dict(au.os.environ, {}, clear=True):
            self.assertEqual(self.execute(), 0)
        self.assertEqual(self.state_path.read_text(), self.initial_state)


if __name__ == "__main__":
    unittest.main()
