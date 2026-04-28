# Awesome-Robot-Learning-from-Human-Videos [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

**Overview.** This repository provides a curated reading list for **robot learning from human videos (LfHV)**, with an emphasis on human-robot skill transfer techniques **in task, observation, and action levels**. 

This repository also includes works on **human-object interaction analysis** and **human video sources** that are widely used in the literature.

Papers with **publicly released code** are marked with a star 🌟. Papers with **real-world robot experiments** are marked with a robot 🤖.

The relevant survey paper is coming soon. Your patience is appreciated.

> Contributions are welcome. If you find missing papers or inaccurate classifications, feel free to open a pull request or contact me via [email](mailto:junyi.ma@sjtu.edu.cn).

![teaser](teaser.png)

## Table of Contents

- [Human-Robot Skill Transfer](#human-robot-skill-transfer)
  - [Task-Oriented Transfer](#task-oriented-transfer)
  - [Observation-Oriented Transfer](#observation-oriented-transfer)
  - [Action-Oriented Transfer](#action-oriented-transfer)
- [Data Foundations](#data-foundations)
  - [Open-Source Datasets](#open-source-datasets)
  - [Human Video Generation](#human-video-generation)
  - [HOI Analysis Techniques](#hoi-analysis-techniques)


## Human-Robot Skill Transfer

### Task-Oriented Transfer
This section covers methods that infer task structures and intents from human videos to guide robot decision-making at the task level.

#### 2026

- 🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.04600)] Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data [Code] [[Page](https://jern-li.github.io/asa/)] [`Task intents`]

#### 2025

- 🤖 [[IJRR](https://journals.sagepub.com/doi/abs/10.1177/02783649251377335)] FMimic: Foundation Models Are Fine-Grained Action Learners from Human Videos [Code] [[Page](https://fmimic-page.github.io/)] [`Task structures`]
- 🤖 [[ICRA](https://ieeexplore.ieee.org/document/11128270)] Chain-of-Modality: Learning Manipulation Programs from Multimodal Human Videos with Vision-Language-Models [Code] [[Page](https://chain-of-modality.github.io/)] [`Task structures`]
- 🤖 [[CoRL](https://proceedings.mlr.press/v305/clark25a.html)] Action-Free Reasoning for Policy Generalization [Code] [[Page](https://rad-generalization.github.io/)] [`Task structures`]
- [[ICASSP](https://ieeexplore.ieee.org/document/10887717)] Interactive Robot Action Replanning Using Multimodal LLM Trained from Human Demonstration Videos [Code] [[Page]] [`Task structures`]
- 🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.16793)] PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence [Code] [[Page](https://zgc-embodyai.github.io/PhysBrain/)] [`Task structures`]
- [[arXiv 2025.11](https://arxiv.org/abs/2511.17335)] Robot Confirmation Generation and Action Planning Using Long-Context Q-Former Integrated with Multimodal LLM [Code] [[Page]] [`Task structures`]
- 🌟🤖 [[arXiv 2025.09](https://arxiv.org/abs/2509.22205)] From Watch to Imagine: Steering Long-Horizon Manipulation via Human Demonstration and Future Envisionment [[Code](https://yipko.com/super-mimic/)] [[Page](https://yipko.com/super-mimic/)] [`Task structures`]
- 🌟🤖 [[arXiv 2025.08](https://arxiv.org/abs/2508.12349)] EgoLoc: A Generalizable Solution for Temporal Interaction Localization in Egocentric Videos [[Code](https://github.com/IRMVLab/EgoLoc)] [[Page]] [`Task structures`]

#### 2024

- 🌟🤖 [[RA-L](https://ieeexplore.ieee.org/document/10711245/)] GPT-4V(ision) for Robotics: Multimodal Task Planning From Human Demonstration [[Code](https://github.com/microsoft/GPT4Vision-Robot-Manipulation-Prompts)] [[Page](https://microsoft.github.io/GPT4Vision-Robot-Manipulation-Prompts/)] [`Task structures`]
- 🤖 [[NeurIPS](https://neurips.cc/virtual/2024/poster/96165)] VLMimic: Vision Language Models Are Visual Imitation Learner for Fine-Grained Actions [Code] [[Page](https://vlmimic.github.io/)] [`Task structures`]
- 🤖 [[RSS](https://www.roboticsproceedings.org/rss20/p052.html)] Vid2Robot: End-to-End Video-Conditioned Policy Learning with Cross-Attention Transformers [Code] [[Page](https://vid2robot.github.io/)] [`Task intents`]
- 🌟🤖 [[IROS](https://ieeexplore.ieee.org/document/10802511)] Knowledge-Based Programming by Demonstration Using Semantic Action Models for Industrial Assembly [[Code](https://github.com/kb-pbd/kb-pbd)] [[Page](https://kb-pbd.github.io/)] [`Task structures`]
- 🌟🤖 [[arXiv 2024.10](https://arxiv.org/abs/2410.08792)] VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model [[Code](https://github.com/ai4ce/SeeDo)] [[Page](https://ai4ce.github.io/SeeDo/)] [`Task structures`]

#### 2023

- 🌟🤖 [[CoRL](https://openreview.net/forum?id=8L6pHd9aS6w)] XSkill: Cross Embodiment Skill Discovery [[Code](https://github.com/real-stanford/xskill)] [[Page](https://xskill.cs.columbia.edu/)] [`Task intents`]
- 🤖 [[arXiv 2023.12](https://arxiv.org/abs/2312.15346)] Learning Multi-Step Manipulation Tasks from A Single Human Demonstration [Code] [[Page]] [`Task structures`]

#### 2022

- 🤖 [[T-MECH](https://ieeexplore.ieee.org/document/9772011/)] Explicit-to-Implicit Robot Imitation Learning by Exploring Visual Content Change [Code] [[Page](https://vsislab.github.io/explicit2implicit/)] [`Task structures`]
- 🤖 [[ICRA](https://ieeexplore.ieee.org/abstract/document/9812402)] Learning Periodic Tasks from Human Demonstrations [Code] [[Page](https://yjy0625.github.io/projects/viptl/)] [`Task structures`]
- 🤖 [[CoRL](https://proceedings.mlr.press/v164/jang22a.html)] BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning [Code] [[Page](https://sites.google.com/view/bc-z/home)] [`Task intents`]
- 🌟 [[CoRL](https://proceedings.mlr.press/v205/pertsch23a.html)] Cross-Domain Transfer via Semantic Skill Imitation [[Code](https://github.com/kpertsch/star)] [[Page](https://kpertsch.github.io/star/)] [`Task structures`]

#### 2019

- 🌟🤖 [[NeurIPS](https://proceedings.neurips.cc/paper/2019/hash/8a146f1a3da4700cbf03cdc55e2daae6-Abstract.html)] Third-Person Visual Imitation Learning via Decoupled Hierarchical Controller [[Code](https://github.com/pathak22/hierarchical-imitation)] [[Page](https://pathak22.github.io/hierarchical-imitation/)] [`Task intents`]
- 🤖 [[IROS](https://ieeexplore.ieee.org/document/8968278/)] Learning Actions from Human Demonstration Video for Robotic Manipulation [Code] [[Page]] [`Task structures`]

#### 2018

- 🤖 [[RSS](https://www.roboticsproceedings.org/rss14/p02.html)] One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning [Code] [[Page]] [`Task intents`]
- 🌟🤖 [[ICRA](https://ieeexplore.ieee.org/document/8460857/)] Translating Videos to Commands for Robotic Manipulation with Deep Recurrent Neural Networks [[Code](https://github.com/nqanh/video2command)] [[Page]] [`Task structures`]
- 🤖 [[arXiv 2018.10](https://arxiv.org/abs/1810.11043)] One-Shot Hierarchical Imitation Learning of Compound Visuomotor Tasks [Code] [[Page](https://sites.google.com/view/one-shot-hil)] [`Task intents`]

#### 2017

- 🌟🤖 [[RSS](https://www.roboticsproceedings.org/rss13/p50.html)] Unsupervised Perceptual Rewards for Imitation Learning [[Code](https://github.com/sermanet/rewards)] [[Page](https://sermanet.github.io/rewards/)] [`Task intents`]
- [[RA-L](https://ieeexplore.ieee.org/document/7856986/)] Unsupervised Linking of Visual Features to Textual Descriptions in Long Manipulation Activities [Code] [[Page]] [`Task structures`]

#### 2015

- [[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/9671)] Robot Learning Manipulation Action Plans by "Watching" Unconstrained Videos from the World Wide Web [Code] [[Page]] [`Task structures`]


### Observation-Oriented Transfer
This section focuses on bridging the observation gap between humans and robots via transformed videos and visual embeddings.


#### 2026

- 🤖 [[Science Robotics](https://www.science.org/doi/10.1126/scirobotics.ady2869)] Visual-Tactile Pretraining and Online Multitask Learning for Humanlike Manipulation Dexterity [Code] [Page] [`Visual embeddings`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2508.09976)] Masquerade: Learning from In-the-Wild Human Videos Using Data-Editing [[Code](https://github.com/MarionLepert/phantom)] [[Page](https://masquerade-robot.github.io/)] [`Transformed videos`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2509.09769)] MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos [[Code](https://github.com/UT-Austin-RPL/mimicdroid-robocasa)] [[Page](https://ut-austin-rpl.github.io/MimicDroid)] [`Visual embeddings`]
- 🤖 [[arXiv 2026.04](https://arxiv.org/abs/2604.10809)] WARPED: Wrist-Aligned Rendering for Robot Policy Learning from Egocentric Human Demonstrations [Code] [Page] [`Transformed videos`]

#### 2025

- 🤖 [[NeurIPS](https://arxiv.org/abs/2509.19626)] EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data [Code] [[Page](https://ego-bridge.github.io/)] [`Visual embeddings`]
- 🌟🤖 [[CVPR](https://arxiv.org/abs/2406.14235)] Mitigating the Human-Robot Domain Discrepancy in Visual Pre-Training for Robotic Manipulation [[Code](https://github.com/jiaming-zhou/HumanRobotAlign)] [[Page](https://jiaming-zhou.github.io/projects/HumanRobotAlign/)] [`Visual embeddings`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2409.06615)] One-Shot Imitation Under Mismatched Execution [[Code](https://github.com/portal-cornell/rhyme)] [[Page]](https://portal-cornell.github.io/rhyme/) [`Visual embeddings`]
- 🌟 [[IROS](https://arxiv.org/abs/2507.19817)] Ag2x2: Robust Agent-Agnostic Visual Representations for Zero-Shot Bimanual Manipulation [[Code](https://github.com/ziyin-xiong/Ag2x2)] [[Page](https://ziyin-xiong.github.io/ag2x2.github.io/)] [`Transformed videos`]
- 🤖 [[IROS](https://arxiv.org/abs/2501.03606)] VTAO-BiManip: Masked Visual-Tactile-Action Pre-Training with Object Understanding for Bimanual Dexterous Manipulation [Code] [Page] [`Visual embeddings`]
- 🤖 [[CoRL](https://arxiv.org/abs/2509.00361)] Generative Visual Foresight Meets Task-Agnostic Pose Estimation in Robotic Table-Top Manipulation [[Code1](https://github.com/Xiaoxiongzzzz/GVF-TAPE)] [[Code2](https://github.com/Xiaoxiongzzzz/GVF-TAPE-Video-Generation)] [[Page](https://clearlab-sustech.github.io/gvf-tape/)] [`Visual embeddings`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2509.10952)] ImMimic: Cross-Domain Imitation from Human Videos via Mapping and Interpolation [[Code](https://github.com/GaTech-RL2/ImMimic-CoRL2025)] [[Page](https://sites.google.com/view/immimic)] [`Visual embeddings`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2503.00779)] Phantom: Training Robots Without Robots Using Only Human Videos [[Code](https://github.com/MarionLepert/phantom)] [[Page](https://phantom-human-videos.github.io/)] [`Transformed videos`]
- 🤖 [[CoRL](https://arxiv.org/abs/2505.20795)] Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt [Code] [Page] [`Visual embeddings`]
- 🌟 [[arXiv 2025.12](https://arxiv.org/abs/2512.09406)] H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos [[Code](https://github.com/showlab/H2R-Grounder)] [[Page](https://showlab.github.io/H2R-Grounder/)] [`Transformed videos`]
- 🌟 [[arXiv 2025.12](https://arxiv.org/abs/2512.17253)] Mitty: Diffusion-Based Human-to-Robot Video Generation [[Code](https://github.com/showlab/Mitty)] [[Page](https://huggingface.co/datasets/showlab/Mitty_Dataset)] [`Transformed videos`]
- 🌟 [[arXiv 2025.12](https://arxiv.org/abs/2512.04537)] X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale [[Code](https://github.com/showlab/X-Humanoid)] [[Page](https://showlab.github.io/X-Humanoid/)] [`Transformed videos`]
- 🌟🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.15692)] mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs [[Code](https://github.com/mimic-video/mimic-video)] [[Page](https://mimic-video.github.io/)] [`Visual embeddings`]
- 🌟🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.13644)] World Models Can Leverage Human Videos for Dexterous Manipulation [[Code](https://github.com/facebookresearch/dexwm)] [[Page](https://raktimgg.github.io/dexwm/)] [`Visual embeddings`]
- 🤖 [[arXiv 2025.10](https://arxiv.org/abs/2510.07773)] Trajectory-Conditioned Cross-Embodiment Skill Transfer [Code] [Page] [`Transformed videos`]
- 🌟🤖 [[arXiv 2025.09](https://arxiv.org/abs/2509.22199)] MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training [[Code](https://github.com/GigaAI-research/MimicDreamer)] [[Page](https://mimicdreamer.github.io/)] [`Transformed videos`]
- 🌟🤖 [[arXiv 2025.09](https://arxiv.org/abs/2509.15212)] RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation [[Code](https://github.com/alibaba-damo-academy/RynnVLA-001)] [[Page](https://huggingface.co/blog/Alibaba-DAMO-Academy/rynnvla-001)] [`Visual embeddings`]
- 🤖 [[arXiv 2025.05](https://arxiv.org/abs/2505.11920)] H2R: A Human-to-Robot Data Augmentation for Robot Pre-Training from Videos [Code] [Page] [`Transformed videos`]

#### 2024

- 🤖 [[T-ASE](https://arxiv.org/abs/2408.05485)] Contrast, Imitate, Adapt: Learning Robotic Skills from Raw Human Videos [Code] [Page] [`Visual embeddings`]
- 🌟🤖 [[ICLR](https://arxiv.org/abs/2312.13139)] Unleashing Large-Scale Video Generative Pre-Training for Visual Robot Manipulation [[Code](https://github.com/bytedance/GR-1)] [[Page](https://gr1-manipulation.github.io/)] [`Visual embeddings`]
- 🤖 [[RSS](https://arxiv.org/abs/2403.12943)] Vid2Robot: End-to-End Video-Conditioned Policy Learning with Cross-Attention Transformers [Code] [[Page](https://vid2robot.github.io/)] [`Visual embeddings`]
- 🌟🤖 [[RSS](https://arxiv.org/abs/2406.00439)] Learning Manipulation by Predicting Interaction [[Code](https://github.com/OpenDriveLab/MPI)] [[Page](https://opendrivelab.com/MPI/)] [`Visual embeddings`]
- [[ICRA](https://ieeexplore.ieee.org/document/10610933/)] Masked Visual-Tactile Pre-Training for Robot Manipulation [Code] [Page] [`Visual embeddings`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2309.13041)] Robotic Offline RL from Internet Videos via Value-Function Pre-Training [[Code](https://github.com/DreekFire/V-PTR)] [[Page](https://dibyaghosh.com/vptr/)] [`Visual embeddings`]
- 🌟🤖 [[IROS](https://arxiv.org/abs/2404.17521)] Ag2Manip: Learning Novel Manipulation Skills with Agent-Agnostic Visual and Action Representations [[Code](https://github.com/xiaoyao-li/Ag2Manip)] [[Page](https://xiaoyao-li.github.io/research/ag2manip/)] [`Transformed videos`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2312.12444)] What Makes Pre-Trained Visual Representations Successful for Robust Manipulation? [[Code](https://github.com/stanford-iris-lab/segmenting_feats/tree/eval)] [[Page](https://kayburns.github.io/segmentingfeatures/)] [`Visual embeddings`]
- 🤖 [[arXiv 2024.10](https://arxiv.org/abs/2410.06158)] GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation [Code] [[Page](https://gr2-manipulation.github.io/)] [`Visual embeddings`]

#### 2023

- 🌟🤖 [[ICML](https://arxiv.org/abs/2306.00958)] LIV: Language-Image Representations and Rewards for Robotic Control [[Code](https://github.com/penn-pal-lab/LIV)] [[Page](https://penn-pal-lab.github.io/LIV/)] [`Visual embeddings`]
- 🌟🤖 [[ICLR](https://arxiv.org/abs/2210.00030)] VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training [[Code](https://github.com/facebookresearch/vip)] [[Page](https://sites.google.com/view/vip-rl)] [`Visual embeddings`]
- 🌟🤖 [[NeurIPS](https://arxiv.org/abs/2305.16301)] Look Ma, No Hands! Agent-Environment Factorization of Egocentric Videos [[Code](https://github.com/MatthewChang/agent_inpainting)] [[Page](matthewchang.github.io/vidm/)] [`Transformed videos`]
- 🌟🤖 [[NeurIPS](https://arxiv.org/abs/2303.18240)] Where Are We in the Search for an Artificial Visual Cortex for Embodied Intelligence? [[Code](https://github.com/facebookresearch/eai-vc)] [[Page](https://eai-vc.github.io/)] [`Visual embeddings`]
- 🤖 [[RSS](https://arxiv.org/abs/2308.10901)] Structured World Models from Human Videos [Code] [[Page](https://human-world-model.github.io/)] [`Visual embeddings`]
- 🌟🤖 [[RSS](https://arxiv.org/abs/2302.12766)] Language-Driven Representation Learning for Robotics [[Code](https://github.com/siddk/voltron-robotics)] [[Page](https://sites.google.com/view/voltron-robotics)] [`Visual embeddings`]
- [[ICRA](https://arxiv.org/abs/2305.06289)] Learning Video-Conditioned Policies for Unseen Manipulation Tasks [Code] [[Page](https://www.di.ens.fr/willow/research/vip/)] [`Visual embeddings`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2306.13818)] AR2-D2: Training a Robot Without a Robot [[Code](https://github.com/jiafei1224/AR2-D2)] [[Page](https://ar2d2.site/)] [`Transformed videos`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2310.09289)] An Unbiased Look at Datasets for Visuo-Motor Pre-Training [[Code](https://github.com/SudeepDasari/data4robotics)] [[Page](https://data4robotics.github.io/)] [`Visual embeddings`]
- 🤖 [[arXiv 2023.04](https://arxiv.org/abs/2304.11801)] Efficient Robot Skill Learning with Imitation from a Single Video for Contact-Rich Fabric Manipulation [Code] [Page] [`Visual embeddings`]

#### 2022

- 🌟🤖 [[CoRL](https://arxiv.org/abs/2203.12601)] R3M: A Universal Visual Representation for Robot Manipulation [[Code](https://github.com/facebookresearch/r3m)] [[Page](https://sites.google.com/view/robot-r3m/)] [`Visual embeddings`]
- 🤖 [[RSS](https://arxiv.org/abs/2207.09450)] Human-to-Robot Imitation in the Wild [Code] [[Page](https://human2robot.github.io/)] [`Transformed videos`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2210.03109)] Real-World Robot Learning with Masked Visual Pre-Training [[Code](https://github.com/ir413/mvp)] [[Page](https://tetexiao.com/projects/real-mvp)] [`Visual embeddings`]
- 🤖 [[CoRL](https://proceedings.mlr.press/v205/xiong23a.html)] RoboTube: Learning Household Manipulation from Human Videos with Simulated Twin Environments [Code] [[Page](https://sites.google.com/view/robotube)] [`Visual embeddings`]
- [[Machines](https://www.mdpi.com/2075-1702/10/11/1049)] Learning by Watching via Keypoint Extraction and Imitation Learning [Code] [Page] [`Transformed videos`]
- 🌟 [[arXiv 2022.03](https://arxiv.org/abs/2203.06173)] Masked Visual Pre-Training for Motor Control [[Code](https://github.com/ir413/mvp)] [[Page](https://tetexiao.com/projects/mvp)] [`Visual embeddings`]

#### 2021

- 🌟🤖 [[RSS](https://arxiv.org/abs/2103.16817)] Learning Generalizable Robotic Reward Functions from "In-the-Wild" Human Videos [[Code](https://github.com/anniesch/dvd)] [[Page](https://sites.google.com/view/dvd-human-videos)] [`Visual embeddings`]
- [[IROS](https://ieeexplore.ieee.org/abstract/document/9636080)] Learning by Watching: Physical Imitation of Manipulation Skills from Human Videos [Code] [[Page](https://www.pair.toronto.edu/lbw-kp/)] [`Transformed videos`]
- 🌟 [[CoRL](https://arxiv.org/abs/2106.03911)] XIRL: Cross-Embodiment Inverse Reinforcement Learning [[Code](https://github.com/google-research/google-research/tree/master/xirl)] [[Page](https://x-irl.github.io/)] [`Visual embeddings`]
- 🤖 [[arXiv 2021.03](https://arxiv.org/abs/2103.09016)] Manipulator-Independent Representations for Visual Imitation [Code] [[Page](https://sites.google.com/view/mir4vi)] [`Transformed videos`]

#### 2020

- 🤖 [[RSS](https://arxiv.org/abs/1912.04443)] AVID: Learning Multi-Stage Tasks Via Pixel-Level Translation of Human Videos [Code] [[Page](https://sites.google.com/view/rss20avid)] [`Transformed videos`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2011.06507)] Reinforcement Learning with Videos: Combining Offline Observations with Interaction [[Code](https://github.com/kschmeckpeper/rl_with_videos)] [[Page](https://sites.google.com/view/rl-with-videos)] [`Visual embeddings`]

#### 2018
- 🌟🤖 [[RA-L](https://arxiv.org/abs/1801.04134)] Deep Episodic Memory: Encoding, Recalling, and Predicting Episodic Experiences for Robot Action Execution [[Code](https://github.com/jonasrothfuss/DeepEpisodicMemory)] [[Page](http://h2t-projects.webarchiv.kit.edu/projects/episodicmemory)] [`Visual embeddings`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/1707.03374)] Imitation from Observation: Learning to Imitate Behaviors from Raw Video via Context Translation [[Code](https://github.com/wyndwarrior/imitation_from_observation)] [[Page](https://sites.google.com/site/imitationfromobservation/)] [`Visual embeddings`]

#### 2017
- 🌟🤖 [[CVPRW](https://ieeexplore.ieee.org/document/8014803)] Time-Contrastive Networks: Self-Supervised Learning from Multi-view Observation [[Code](https://github.com/kekeblom/tcn)] [[Page](https://sermanet.github.io/imitate/)] [`Visual embeddings`]

### Action-Oriented Transfer
This section includes methods that transfer actionable motion knowledge from human videos to robot control, including affordances (explicit interaction info) and latent actions.


#### 2026

- 🌟🤖 [[TRO&IROS](https://arxiv.org/abs/2503.06669)] AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems [[Code](https://github.com/OpenDriveLab/AgiBot-World)] [[Page](https://agibot-world.com/)] [`Latent actions`]
- 🌟🤖 [[ICLR&NeurIPS Workshop](https://arxiv.org/abs/2511.07732)] ViPRA: Video Prediction for Robot Actions [[Code](https://github.com/sroutray/vipra)] [[Page](https://vipra-project.github.io/)] [`Latent actions`]
- 🌟🤖 [[CVPR](https://arxiv.org/abs/2602.21736)] Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild [[Code](https://github.com/BeingBeyond/JALA)] [[Page](https://research.beingbeyond.com/jala)] [`Latent actions`]
- 🌟🤖 [[CVPR](https://arxiv.org/abs/2603.22264)] UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos [[Code](https://github.com/unidex-ai/UniDex)] [[Page](https://unidex-ai.github.io/)][`Affordances`]
- 🌟🤖 [[CVPR](https://arxiv.org/abs/2512.13080)] Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos [[Code](https://github.com/BeingBeyond/VIPA-VLA)] [[Page](https://beingbeyond.github.io/VIPA-VLA/)] [`Affordances`]
- 🌟🤖 [[AAAI](https://arxiv.org/abs/2507.23523)] H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation [[Code](https://github.com/HongzheBi/H_RDT)] [[Page](https://embodiedfoundation.github.io/hrdt)] [`Affordances`]
- 🌟 [[AAAI](https://arxiv.org/abs/2508.08896)] Towards Affordance-Aware Robotic Dexterous Grasping with Human-Like Priors [[Code](https://github.com/Maxwell-Zhao/AffordDex/)] [[Page](https://afforddex.github.io/)] [`Affordances`]
- [[ICASSP](https://arxiv.org/abs/2601.22467)] CARE: Multi-Task Pretraining for Latent Continuous Action Representation in Robot Control [Code] [Page] [`Latent actions`]
- 🤖 [[RA-L](https://arxiv.org/abs/2509.04443)] EMMA: Scaling Mobile Manipulation via Egocentric Human Data [Code] [[Page](https://ego-moma.github.io/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2509.15212)] RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation [[Code](https://github.com/alibaba-damo-academy/RynnVLA-001)] [Page] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2506.20668)] DemoDiffusion: One-Shot Human Imitation Using Pre-Trained Diffusion Policy [[Code](https://github.com/demodiffusion/demodiffusion)] [[Page](https://demodiffusion.github.io/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2510.08568)] NovaFlow: Zero-Shot Manipulation via Actionable Flow from Generated Videos [[Code](https://github.com/rai-opensource/NovaFlow/)] [[Page](https://novaflow.lhy.xyz/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2510.12971)] Actron3D: Learning Actionable Neural Functions from Videos for Transferable Robotic Manipulation [[Code](https://github.com/ethz-mrl/Actron3D)] [[Page](https://dipan-zhang.github.io/Actron3D-project/)] [`Affordances`]
- 🤖 [[arXiv 2026.04](https://arxiv.org/abs/2604.08534)] ActiveGlasses: Learning Manipulation with Active Vision from Ego-centric Human Demonstration [Code] [[Page](https://yanwen-zou.github.io/activeglasses/)] [`Affordances`]
- 🌟🤖 [[arXiv 2026.04](https://arxiv.org/abs/2604.16391)] Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining [[Code](https://github.com/LogosRoboticsGroup/DeFi)] [[Page](https://huggingface.co/zbzzbz/DeFI)] [`Latent actions`]
- 🌟🤖 [[arXiv 2026.03](https://arxiv.org/abs/2603.25539)] PAWS: Perception of Articulation in the Wild at Scale from Egocentric Videos [[Code](https://github.com/AaltoML/PAWS)] [[Page](https://aaltoml.github.io/PAWS/)] [`Affordances`]
- 🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.16710)] EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data [Code] [[Page](https://research.nvidia.com/labs/gear/egoscale/)] [`Affordances`]
- [[arXiv 2026.02](https://arxiv.org/abs/2602.03668)] MVP-LAM: Learning Action-Centric Latent Action via Cross-Viewpoint Reconstruction [Code] [Page] [`Latent actions`]
- 🌟🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.06949)] DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos [[Code](https://github.com/NVIDIA/DreamDojo)] [[Page](https://dreamdojo-world.github.io/)] [`Latent actions`]
- 🌟🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.20231)] UniLACT: Depth-Aware RGB Latent Action Learning for Vision-Language-Action Models [[Code](https://github.com/ManishGovind/UniLACT)] [[Page](https://manishgovind.github.io/unilact-vla/)] [`Latent actions`]
- 🌟🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.10098)] VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model [[Code](https://github.com/ginwind/VLA-JEPA)] [[Page](https://ginwind.github.io/VLA-JEPA/)] [`Latent actions`]
- 🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.09013)] Dexterous Manipulation Policies from RGB Human Videos via 3D Hand-Object Trajectory Reconstruction [Code] [[Page](https://videomanip.github.io/)] [`Affordances`]
- 🌟🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.00557)] ConLA: Contrastive Latent Action Learning from Human Videos for Robotic Manipulation [[Code](https://github.com/WeishengDAI/ConLA)] [Page] [`Latent actions`]
- 🌟🤖 [[arXiv 2026.02](https://arxiv.org/abs/2602.12215)] LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion [[Code](https://github.com/jiangranlv/LDA-1B)] [[Page](https://pku-epic.github.io/LDA/)] [`Latent actions`]
- 🌟🤖 [[arXiv 2026.01](https://arxiv.org/abs/2601.12993)] Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization [[Code](https://github.com/BeingBeyond/Being-H/tree/main/Being-H05)] [[Page](https://research.beingbeyond.com/being-h05)][`Affordances`]
- [[arXiv 2026.01](https://arxiv.org/abs/2601.05230)] Learning Latent Action World Models in the Wild [Code] [Page] [`Latent actions`]
- [[arXiv 2026.01](https://arxiv.org/abs/2601.05237)] ObjectForesight: Predicting Future 3D Object Trajectories from Human Videos [Code] [[Page](https://objectforesight.github.io/)] [`Affordances`]
- 🤖 [[arXiv 2026.01](https://arxiv.org/abs/2601.04061)] CLAP: Contrastive Latent Action Pretraining for Learning Vision-Language-Action Models from Human Videos [Code] [[Page](https://lin-shan.com/CLAP/)] [`Latent actions`]

#### 2025

- 🌟🤖 [[CVPR](https://arxiv.org/abs/2503.21860)] ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning [[Code](https://github.com/ManipTrans/ManipTrans)] [[Page](https://maniptrans.github.io/)] [`Affordances`]
- 🌟🤖 [[CVPR](https://arxiv.org/abs/2411.14519)] Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning [[Code](https://github.com/MCG-NJU/Tra-MoE)] [Page] [`Affordances`]
- 🤖 [[CVPR](https://arxiv.org/abs/2507.25743)] GraphMimic: Graph-to-Graphs Generative Modeling from Videos for Policy Learning [Code] [Page] [`Affordances`]
- 🌟🤖 [[CVPR](https://arxiv.org/abs/2503.07135)] VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation [[Code](https://github.com/ethz-mrl/VidBot)] [[Page](https://hanzhic.github.io/vidbot-project/)] [`Affordances`]
- 🌟🤖 [[ICCV](https://arxiv.org/abs/2508.07626)] AR-VRM: Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning [[Code](https://github.com/github-sxiong/AR-VRM-Imitating-Human-Motions-for-Visual-Robot-Manipulation-with-Analogical-Reasoning)] [[Page](https://idejie.com/AR/)] [`Affordances`]
- 🌟🤖 [[ICCV](https://arxiv.org/pdf/2506.23152)] DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover [[Code](https://github.com/4DVLab/DexH2R)] [[Page](https://dexh2r.github.io/)] [`Affordances`]
- 🌟🤖 [[ICCV](https://arxiv.org/abs/2412.04445)] Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos [[Code](https://github.com/TencentARC/Moto)] [[Page](https://chenyi99.github.io/moto/)] [`Latent actions`]
- 🌟🤖 [[ICCV&CoRL Workshop](https://arxiv.org/abs/2503.09320)] 2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos [[Code](https://github.com/pearl-robot-lab/2HandedAfforder)] [[Page](https://sites.google.com/view/2handedafforder)] [`Affordances`]
- 🌟🤖 [[RSS](https://arxiv.org/abs/2505.06111)] UniVLA: Learning to Act Anywhere with Task-Centric Latent Actions [[Code](https://github.com/OpenDriveLab/UniVLA)] [Page] [`Latent actions`]
- 🤖 [[RSS](https://arxiv.org/abs/2501.14208)] You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations [[Code](https://github.com/hnuzhy/YOTO)] [[Page](https://hnuzhy.github.io/projects/YOTO)] [`Affordances`]
- 🤖 [[RSS Workshop](https://arxiv.org/abs/2505.01288)] ViSA-Flow: Accelerating Robot Skill Learning via Large-Scale Video Semantic Action Flow [Code] [Page] [`Affordances`]
- [[RSS Workshop](https://arxiv.org/abs/2512.00024)] Learning from Watching: Scalable Extraction of Manipulation Trajectories from Human Videos [Code] [Page] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2404.15709)] ViViDex: Learning Vision-Based Dexterous Manipulation from Human Videos [[Code](https://github.com/zerchen/vividex_mujoco,https://github.com/zerchen/vividex_sapien)] [[Page](https://zerchen.github.io/projects/vividex.html)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/pdf/2407.12957v2)] R+X: Retrieval and Execution from Everyday Human Videos [[Code](https://github.com/gpapagiannis/r-plus-x-hand2actions)] [[Page](https://www.robot-learning.uk/r-plus-x)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2503.23877)] ZeroMimic: Distilling Robotic Manipulation Skills from Web Videos [[Code](https://github.com/junyaoshi/ZeroMimic)] [[Page](https://zeromimic.github.io/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2411.00965)] SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation [[Code](https://github.com/NVlabs/object_centric_diffusion)] [[Page](https://nvlabs.github.io/object_centric_diffusion/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2410.23289)] Bridging the Human to Robot Dexterity Gap through Object-Oriented Rewards [[Code](https://github.com/irmakguzey/object-rewards/tree/main)] [[Page](https://object-rewards.github.io/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2410.24221v1)] EgoMimic: Scaling Imitation Learning via Egocentric Video [[Code](https://github.com/SimarKareer/EgoMimic)] [[Page](https://egomimic.github.io/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2501.06994)] Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning [[Code](https://github.com/jren03/mt_pi_codebase)] [[Page](https://portal-cornell.github.io/motion_track_policy/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2409.08273)] Hand-Object Interaction Pretraining from Videos [[Code](https://github.com/hgaurav2k/hop)] [[Page](https://hgaurav2k.github.io/hop/)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2409.08273)] Hand-Object Interaction Pretraining from Videos [[Code](https://github.com/hgaurav2k/hop)] [[Page](https://hgaurav2k.github.io/hop/)] [`Latent actions`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2509.19958)] Generalist Robot Manipulation beyond Action Labeled Data [[Code](https://github.com/insait-institute/motovla)] [[Page](https://motovla.insait.ai/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2511.15704)] In-N-On: Scaling Egocentric Manipulation with In-the-Wild and On-Task Data [[Code](https://github.com/XiongyiCai/Human0)] [[Page](https://xiongyicai.github.io/In-N-On/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2503.13441)] Humanoid Policy ~ Human Policy [[Code](https://github.com/RogerQi/human-policy)] [[Page](https://human-as-robot.github.io/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2505.07096)] X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real [[Code](https://github.com/portal-cornell/X-Sim)] [[Page](https://portal-cornell.github.io/X-Sim/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2504.12609)] Crossing the Human-Robot Embodiment Gap with Sim-to-Real RL Using One Human Demonstration [[Code](https://github.com/tylerlum/human2sim2robot)] [[Page](https://human2sim2robot.github.io/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2502.11744)] FUNCTO: Function-Centric One-Shot Imitation Learning for Tool Manipulation [[Code](https://github.com/mkt1412/FUNCTO_public)] [[Page](https://sites.google.com/view/functo)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2508.13534)] MimicFunc: Imitating Tool Manipulation from a Single Human Video via Functional Correspondence [[Code](https://github.com/mkt1412/FUNCTO_public)] [[Page](https://sites.google.com/view/mimicfunc)] [`Affordances`]
- 🌟 [[CoRL](https://arxiv.org/abs/2509.01708)] Articulated Object Estimation in the Wild [[Code](https://github.com/robot-learning-freiburg/artipoint)] [[Page](https://artipoint.cs.uni-freiburg.de/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2502.20391)] Point Policy: Unifying Observations and Actions with Key Points for Robot Manipulation [[Code](https://github.com/siddhanthaldar/Point-Policy)] [[Page](https://point-policy.github.io/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2505.08787)] UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations [[Code](https://github.com/KimHanjung/UniSkill)] [[Page](https://kimhanjung.github.io/UniSkill/)] [`Latent actions`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2401.11439)] General Flow as Foundation Affordance for Scalable Robot Learning [[Code](https://github.com/michaelyuancb/general_flow)] [[Page](https://general-flow.github.io/)] [`Affordances`]
- 🤖 [[CoRL Workshop](https://arxiv.org/abs/2508.20085)] HERMES: Human-to-Robot Embodied Learning from Multi-Source Motion Data for Mobile Dexterous Manipulation [Code] [[Page](https://gemcollector.github.io/HERMES/)] [`Affordances`]
- 🌟🤖 [[Autonomous Robots](https://arxiv.org/abs/2404.17906)] View: Visual Imitation Learning with Waypoints [[Code](https://github.com/VT-Collab/view)] [[Page](https://collab.me.vt.edu/view/)] [`Affordances`]
- 🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.24210)] GR-Dexter Technical Report [Code] [[Page](https://byte-dexter.github.io/gr-dexter/)] [`Affordances`]
- 🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.22414)] Emergence of Human to Robot Transfer in Vision-Language-Action Models [Code] [Page] [`Affordances`]
- 🌟🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.13030)] Motus: A Unified Latent Action World Model [[Code](https://github.com/thu-ml/Motus)] [[Page](https://motus-robotics.github.io/motus)] [`Latent actions`]
- 🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.23162v1)] SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling [Code] [Page] [`Affordances`]
- 🌟🤖 [[arXiv 2025.11](https://arxiv.org/abs/2511.12878)] Uni-Hand: Universal Hand Motion Forecasting in Egocentric Views [[Code](https://github.com/IRMVLab/UniHand)] [[Page](https://irmvlab.github.io/unihand.github.io/)] [`Affordances`]
- 🌟🤖 [[arXiv 2025.11](https://arxiv.org/pdf/2511.16661)] Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations [[Code](https://github.com/facebookresearch/AINA/tree/main)] [[Page](https://aina-robot.github.io/)] [`Affordances`]
- 🤖 [[arXiv 2025.11](https://arxiv.org/abs/2511.23034)] LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models [Code] [[Page](https://mm-robot.github.io/distill_latent_action/)] [`Latent actions`]
- 🤖 [[arXiv 2025.10](https://arxiv.org/abs/2510.21571)] Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos [Code] [Page] [`Affordances`]
- 🌟 [[arXiv 2025.10](https://arxiv.org/abs/2510.08475)] DexMan: Learning Bimanual Dexterous Manipulation from Human and Generated Videos [[Code](https://github.com/EmbodiedAI-NTU/DexMan)] [[Page](https://embodiedai-ntu.github.io/dexman/index.html)] [`Affordances`]
- 🤖 [[arXiv 2025.10](https://arxiv.org/abs/2510.00491)] From Human Hands to Robot Arms: Manipulation Skills Transfer via Trajectory Alignment [Code] [Page] [`Affordances`]
- 🌟🤖 [[arXiv 2025.10](https://arxiv.org/pdf/2510.00491v2)] Traj2Action: A Co-Denoising Framework for Trajectory-Guided Human-to-Robot Skill Transfer [[Code](https://github.com/MicDZ/Traj2Action)] [[Page](https://www.micdz.cn/Traj2Action/)] [`Affordances`]
- 🤖 [[arXiv 2025.09](https://arxiv.org/abs/2509.21986)] Developing Vision-Language-Action Model from Egocentric Videos [Code] [Page] [`Affordances`]
- 🌟🤖 [[arXiv 2025.09](https://arxiv.org/abs/2509.17759)] MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies [[Code](https://github.com/michaelyuancb/motiontrans)] [[Page](https://motiontrans.github.io/)] [`Affordances`]
- 🌟 [[arXiv 2025.08](https://arxiv.org/abs/2508.18691)] Deep Sensorimotor Control by Imitating Predictive Models of Human Motion [[Code](https://github.com/hgaurav2k/trackr)] [[Page](https://jirl-upenn.github.io/track_reward/)] [`Affordances`]
- 🌟 [[arXiv 2025.07](https://arxiv.org/abs/2507.12440)] EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos [[Code](https://github.com/RchalYang/EgoVLA_Release)] [[Page](https://rchalyang.github.io/EgoVLA/)] [`Affordances`]
- 🌟🤖 [[arXiv 2025.07](https://arxiv.org/abs/2507.15597)] Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos [[Code](https://github.com/BeingBeyond/Being-H0)] [[Page](https://beingbeyond.github.io/Being-H0/)] [`Affordances`]
- 🤖 [[arXiv 2025.07](https://arxiv.org/abs/2507.15493)] GR-3 Technical Report [Code] [[Page](https://seed.bytedance.com/zh/GR3)] [`Affordances`]
- 🌟🤖 [[arXiv 2025.07](https://arxiv.org/abs/2507.23682)] villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models [[Code](https://github.com/microsoft/villa-x/)] [[Page](https://microsoft.github.io/villa-x/)] [`Latent actions`]
- 🌟🤖 [[arXiv 2025.06](https://arxiv.org/abs/2506.04227)] Object-Centric 3D Motion Field for Robot Learning from Human Videos [[Code](https://github.com/zhaohengyin/3dmf-mod)] [[Page](https://zhaohengyin.github.io/3DMF/)] [`Affordances`]
- 🌟🤖 [[arXiv 2025.05](https://arxiv.org/abs/2505.20290)] EgoZero: Robot Learning from Smart Glasses [[Code](https://github.com/vliu15/egozero)] [[Page](https://egozero-robot.github.io/)] [`Affordances`]
- 🤖 [[arXiv 2025.05](https://arxiv.org/abs/2505.05517)] Web2Grasp: Learning Functional Grasps from Web Images of Hand-Object Interactions [Code] [[Page](https://web2grasp.github.io/)] [`Affordances`]
- 🤖 [[arXiv 2025.04](https://arxiv.org/abs/2504.01959)] Slot-Level Robotic Placement via Visual Imitation from Single Human Video [Code] [[Page](https://ddshan.github.io/slerp/)] [`Affordances`]
- 🌟🤖 [[arXiv 2025.03](https://arxiv.org/abs/2503.14734)] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots [[Code](https://github.com/NVIDIA/Isaac-GR00T)] [[Page](https://developer.nvidia.com/isaac/gr00t)] [`Affordances`]
- 🤖 [[arXiv 2025.02](https://arxiv.org/abs/2502.09886)] Video2Policy: Scaling Up Manipulation Tasks in Simulation Through Internet Videos [Code] [[Page](https://yewr.github.io/video2policy/)] [`Affordances`]

#### 2024

- 🌟🤖 [[ICLR](https://arxiv.org/abs/2310.08576)] Learning to Act from Actionless Videos through Dense Correspondences [[Code](https://github.com/flow-diffusion/AVDC)] [[Page](https://flow-diffusion.github.io/)] [`Affordances`]
- 🌟🤖 [[ICLR](https://arxiv.org/abs/2410.11758)] Latent Action Pretraining from Videos [[Code](https://github.com/LatentActionPretraining/LAPA)] [[Page](https://latentactionpretraining.github.io/)] [`Latent actions`]
- 🤖 [[ICLR](https://arxiv.org/abs/2311.01977)] RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches [Code] [[Page](https://rt-trajectory.github.io/)] [`Affordances`]
- 🌟🤖 [[ECCV](https://arxiv.org/abs/2405.01527)] Track2Act: Predicting Point Tracks from Internet Videos Enables Generalizable Robot Manipulation [[Code](https://github.com/homangab/Track-2-Act/)] [[Page](https://homangab.github.io/track2act/)] [`Affordances`]
- 🌟🤖 [[ECCV](https://arxiv.org/abs/2401.07487)] Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation [[Code](https://github.com/TEA-Lab/Robo-ABC)] [[Page](https://tea-lab.github.io/Robo-ABC/)] [`Affordances`]
- 🌟🤖 [[RSS](https://arxiv.org/abs/2407.18911)] HRP: Human Affordances for Robotic Pre-Training [[Code](https://github.com/SudeepDasari/data4robotics/tree/hrp_release)] [[Page](https://hrp-robot.github.io/)] [`Affordances`]
- 🌟🤖 [[RSS](https://arxiv.org/abs/2405.03666)] ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection [[Code](https://github.com/UT-Austin-RobIn/ScrewMimic)] [[Page](https://robin-lab.cs.utexas.edu/ScrewMimic/)] [`Affordances`]
- 🤖 [[ICRA](https://arxiv.org/abs/2312.00775)] Towards Generalizable Zero-Shot Manipulation via Translating Human Interaction Plan [Code] [[Page](https://homangab.github.io/hopman/)] [`Affordances`]
- 🌟🤖 [[IROS](https://arxiv.org/abs/2403.15203)] Ditto: Demonstration Imitation by Trajectory Transformation [[Code](https://github.com/robot-learning-freiburg/DITTO)] [[Page](https://ditto.cs.uni-freiburg.de)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2407.04689)] RAM: Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation [[Code](https://github.com/yxKryptonite/RAM_code)] [[Page](https://yuxuank.com/RAM/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2409.18121)] Robot See Robot Do: Imitating Articulated Object Manipulation with Monocular 4D Reconstruction [[Code](https://github.com/kerrj/rsrd)] [[Page](https://robot-see-robot-do.github.io/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2410.11792)] OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation [[Code](https://github.com/UT-Austin-RPL/OKAMI)] [[Page](https://ut-austin-rpl.github.io/OKAMI/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2407.15208)] Im2Flow2Act: Flow as the Cross-Domain Manipulation Interface [[Code](https://github.com/real-stanford/im2Flow2Act)] [[Page](https://im-flow-act.github.io/)] [`Affordances`]
- [[arXiv 2024.11](https://arxiv.org/abs/2411.00785)] IGOR: Image-Goal Representations Are the Atomic Control Units for Foundation Models in Embodied AI [Code] [[Page](https://www.microsoft.com/en-us/research/project/igor-image-goal-representations/)] [`Latent actions`]
- 🤖 [[arXiv 2024.05](https://arxiv.org/abs/2405.20321)] Vision-Based Manipulation from Single Human Video with Open-World Object Graphs [Code] [Page] [`Affordances`]

#### 2023

- 🌟🤖 [[TRO](https://arxiv.org/abs/2209.03277)] K-VIL: Keypoints-Based Visual Imitation Learning [[Code](https://gitlab.com/paper-code/kvil_public)] [[Page](https://sites.google.com/view/k-vil)] [`Affordances`]
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2203.13251)] Dexterous Imitation Made Easy: A Learning-Based Framework for Efficient Dexterous Manipulation [[Code](https://github.com/NYU-robot-learning/DIME-Models)] [[Page](https://nyu-robot-learning.github.io/dime/)] [`Affordances`]
- 🌟🤖 [[CVPR](https://arxiv.org/abs/2304.08488)] Affordances from Human Videos as a Versatile Representation for Robotics [[Code](https://github.com/shikharbahl/vrb)] [[Page](https://robo-affordances.github.io/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2302.12422)] MimicPlay: Long-Horizon Imitation Learning by Watching Human Play [[Code](https://github.com/j96w/MimicPlay)] [[Page](https://mimic-play.github.io/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/abs/2310.19797)] DEFT: Dexterous Fine-Tuning for Hand Policies [[Code](https://github.com/adityak77/deft-data)] [[Page](https://dexterous-finetuning.github.io/)] [`Affordances`]
- 🌟🤖 [[RSS](https://arxiv.org/abs/2401.00025)] Any-Point Trajectory Modeling for Policy Learning [[Code](https://github.com/Large-Trajectory-Model/ATM)] [[Page](https://xingyu-lin.github.io/atm/)] [`Affordances`]
- 🌟🤖 [[RA-L&IROS](https://arxiv.org/abs/2207.05053)] Learning Continuous Grasping Function with a Dexterous Hand from Human Demonstrations [[Code](https://github.com/jianglongye/cgf)] [[Page](https://jianglongye.com/cgf/)] [`Affordances`]
- 🤖 [[ICRA Workshop](https://arxiv.org/abs/2302.02011)] Zero-Shot Robot Manipulation from Passive Human Videos [Code] [[Page](https://sites.google.com/view/human-0shot-robot)] [`Affordances`]
- 🤖 [[Sensors](https://www.mdpi.com/1424-8220/23/5/2514)] Robot Programming from a Single Demonstration for High-Precision Industrial Insertion [Code] [Page] [`Affordances`]

#### 2022

- [[RSS](https://arxiv.org/abs/2201.12716)] You Only Demonstrate Once: Category-Level Manipulation from Single Visual Demonstration [Code] [[Page](https://www.youtube.com/watch?v=WAr8ZY3mYyw)] [`Affordances`]
- 🤖 [[CoRL](https://arxiv.org/abs/2212.04498)] VideoDex: Learning Dexterity from Internet Videos [Code] [[Page](https://video-dex.github.io/)] [`Affordances`]
- 🌟🤖 [[CoRL](https://arxiv.org/pdf/2207.14299)] Graph Inverse Reinforcement Learning from Diverse Videos [[Code](https://github.com/SateeshKumar21/graph-inverse-rl)] [`Affordances`]
- 🤖 [[RSS](https://arxiv.org/abs/2202.10448)] Robotic Telekinesis: Learning a Robotic Hand Imitator by Watching Humans on YouTube [Code] [[Page](https://robotic-telekinesis.github.io/)] [`Affordances`]
- 🌟🤖 [[RA-L&IROS](https://arxiv.org/abs/2204.12490)] From One Hand to Multiple Hands: Imitation Learning for Dexterous Manipulation from Single-Camera Teleoperation [[Code](https://github.com/yzqin/dex-hand-teleop)] [[Page](https://yzqin.github.io/dex-teleop-imitation/)] [`Affordances`]
- 🤖 [[RSS](https://arxiv.org/abs/2207.09450)] Human-to-Robot Imitation in the Wild [Code] [[Page](https://human2robot.github.io/)] [`Affordances`]
- 🌟 [[ECCV](https://arxiv.org/abs/2108.05877)] DexMV: Imitation Learning for Dexterous Manipulation from Human Videos [[Code](https://github.com/yzqin/dexmv-sim)] [[Page](https://yzqin.github.io/dexmv/)] [`Affordances`]
- [[arXiv 2022.11](https://arxiv.org/abs/2211.13225)] Learning to Imitate Object Interactions from Internet Videos [Code] [[Page](https://austinapatel.github.io/imitate-video/)] [`Affordances`]

#### 2021

- [[CoRL](https://arxiv.org/abs/2202.00164)] DexVIP: Learning Dexterous Grasping with Human Hand Pose Priors from Video [Code] [[Page](https://vision.cs.utexas.edu/projects/dexvip-dexterous-grasp-pose-prior/)] [`Affordances`]

#### 2020

- 🤖 [[CoRL](https://arxiv.org/pdf/2010.09034)] Model-Based Inverse Reinforcement Learning from Visual Demonstrations [Code] [[Page](https://neha191091.github.io/publication/2021-01-06-model-based-irl)] [`Affordances`]

#### 2019

- 🤖 [[CoRL](https://arxiv.org/pdf/1907.05518)] Graph-Structured Visual Imitation [Code] [Page] [`Affordances`]

#### 2017

- 🤖 [[CVPR](https://arxiv.org/pdf/1703.01040)] Learning Robot Activities from First-Person Human Videos Using Convolutional Future Regression [Code] [Page] [`Affordances`]


## Data Foundations

### Open-Source Datasets
This section collects open-source human video datasets.

| Dataset | Year | Venue | Website | Viewpoint |
|---|---:|---|---|---|
| [EgoLive](https://arxiv.org/pdf/2604.23570v1) | 2026 | arXiv 2026.04 | [Code] [[Page](https://robotdata-market.jdcloud.com/console/market)] | Ego |
| [DreamDojo-HV](https://arxiv.org/abs/2602.06949) | 2026 | arXiv 2026.02 | [[Code](https://github.com/NVIDIA/DreamDojo)] [[Page](https://dreamdojo-world.github.io/)] | Ego |
| [UniHand-Mix](https://arxiv.org/abs/2602.21736) | 2026 | arXiv 2026.02 | [[Code](https://github.com/BeingBeyond/JALA)] [[Page](https://research.beingbeyond.com/jala)] | Ego |
| [UniHand-2.0](https://arxiv.org/abs/2601.12993) | 2026 | arXiv 2026.01 | [[Code](https://github.com/BeingBeyond/Being-H)] [[Page](https://research.beingbeyond.com/being-h05)] | Ego |
| [Action100M](https://arxiv.org/abs/2601.10592) | 2026 | arXiv 2026.01 | [[Code](https://github.com/facebookresearch/Action100M)] [[Page](https://huggingface.co/datasets/facebook/action100m-preview)] | Ego+Exo |
| [EgoVid-5M](https://arxiv.org/abs/2411.08380) | 2025 | NeurIPS | [[Code](https://github.com/JeffWang987/EgoVid)] [[Page](https://egovid.github.io/)] | Ego |
| [HO-Cap](https://arxiv.org/abs/2406.06843) | 2025 | NeurIPS | [[Code](https://github.com/IRVLUTD/HO-Cap)] [[Page](https://irvlutd.github.io/HOCap/)] | Ego+Exo |
| [IndEgo](https://arxiv.org/abs/2511.19684) | 2025 | NeurIPS | [[Code](https://github.com/Vivek9Chavan/IndEgo)] [[Page](https://huggingface.co/datasets/FraunhoferIPK/IndEgo)] | Ego+Exo |
| [HD-EPIC](https://arxiv.org/abs/2502.04144) | 2025 | CVPR | [[Code](https://github.com/hd-epic/hd-epic-annotations/)] [[Page](https://epic-kitchens.github.io/)] | Ego |
| [HOT3D](https://arxiv.org/abs/2411.19167) | 2025 | CVPR | [[Code](https://github.com/facebookresearch/hot3d)] [[Page](https://facebookresearch.github.io/hot3d/)] | Ego |
| [TASTE-Rob](https://arxiv.org/abs/2503.11423) | 2025 | CVPR | [[Code](https://github.com/GAP-LAB-CUHK-SZ/TASTE-Rob)] [[Page](https://taste-rob.github.io/)] | Ego |
| [LVP-1M](https://arxiv.org/abs/2512.15840) | 2025 | arXiv 2025.12 | [[Code](https://github.com/buoyancy99/large-video-planner/tree/main)] [[Page](https://www.boyuan.space/large-video-planner/)] | Ego+Exo |
| [UniHand-1.0](https://arxiv.org/abs/2507.15597) | 2025 | arXiv 2025.07 | [[Code](https://github.com/BeingBeyond/Being-H0)] [[Page](https://beingbeyond.github.io/Being-H0/)] | Ego |
| [EgoDex](https://arxiv.org/abs/2505.11709) | 2025 | arXiv 2025.05 | [[Code](https://github.com/apple/ml-egodex)] [[Page](https://machinelearning.apple.com/research/egodex-learning-dexterous-manipulation)] | Ego |
| [PH²D](https://arxiv.org/abs/2503.13441) | 2025 | arXiv 2025.03 | [[Code](https://github.com/RogerQi/human-policy)] [[Page](https://human-as-robot.github.io/)] | Ego |
| Egocentric-100k | 2025 | --- | [Code] [[Page](https://huggingface.co/datasets/builddotai/Egocentric-100K)] | Ego |
| Egocentric-10k | 2025 | --- | [Code] [[Page](https://huggingface.co/datasets/builddotai/Egocentric-10K)] | Ego |
| [OakInk2](https://arxiv.org/abs/2403.03328) | 2024 | NeurIPS | [[Code](https://github.com/oakink/OakInk2)] [[Page](https://oakink.net/v2/)] | Ego+Exo |
| [CaptainCook4D](https://arxiv.org/abs/2312.14556) | 2024 | NeurIPS | [[Code](https://github.com/CaptainCook4D/)] [[Page](https://captaincook4d.github.io/captain-cook/)] | Ego |
| [Panda-70M](https://arxiv.org/abs/2402.19479) | 2024 | CVPR | [[Code](https://github.com/snap-research/Panda-70M)] [[Page](https://snap-research.github.io/Panda-70M/)] | Ego+Exo |
| [TACO](https://arxiv.org/abs/2401.08399) | 2024 | CVPR | [[Code](https://github.com/leolyliu/TACO-Instructions)] [[Page](https://taco2024.github.io/)] | Ego+Exo |
| [Ego-Exo4D](https://arxiv.org/abs/2311.18259) | 2024 | CVPR | [[Code](https://ego-exo4d-data.org/)] [[Page](https://ego-exo4d-data.org/)] | Ego+Exo |
| [Nymeria](https://arxiv.org/abs/2406.09326) | 2024 | ECCV | [[Code](https://github.com/facebookresearch/nymeria_dataset)] [[Page](https://www.projectaria.com/datasets/nymeria/)] | Ego+Exo |
| [ARCTIC](https://arxiv.org/abs/2204.13662) | 2023 | CVPR | [[Code](https://github.com/zc-alexfan/arctic)] [[Page](https://arctic.is.tue.mpg.de/)] | Ego+Exo |
| [HoloAssist](https://arxiv.org/abs/2309.17519) | 2023 | ICCV | [[Code](https://github.com/Ember-HoloAssist/holoassist-release)] [[Page](https://holoassist.github.io/)] | Ego |
| [RH20T-Human](https://arxiv.org/abs/2307.00595) | 2023 | ICRA | [[Code](https://github.com/rh20t/rh20t_api)] [[Page](https://rh20t.github.io/#download)] | Ego+Exo |
| [EPIC-KITCHENS-100](https://arxiv.org/abs/2006.13256) | 2022 | IJCV | [[Code](https://github.com/epic-kitchens/epic-kitchens-100-annotations)] [[Page](https://epic-kitchens.github.io/)] | Ego |
| [Assembly101*](https://arxiv.org/abs/2203.14712) | 2022 | CVPR | [[Code](https://github.com/assembly-101?tab=repositories)] [[Page](https://assembly-101.github.io/)] | Ego+Exo |
| [Ego4D](https://arxiv.org/abs/2110.07058) | 2022 | CVPR | [[Code](https://github.com/facebookresearch/Ego4d)] [[Page](https://ego4d-data.org/)] | Ego |
| [OakInk](https://arxiv.org/abs/2203.15709) | 2022 | CVPR | [[Code](https://github.com/oakink/OakInk)] [[Page](https://oakink.net/)] | Exo |
| [HOI4D](https://arxiv.org/abs/2203.01577) | 2022 | CVPR | [[Code](https://github.com/hoi4d/HOI4D_ActionSeg)] [[Page](https://hoi4d.github.io/)] | Ego |
| [EgoPAT3D](https://arxiv.org/abs/2203.13116) | 2022 | CVPR | [[Code](https://github.com/ai4ce/EgoPAT3D)] [[Page](https://ai4ce.github.io/EgoPAT3D/)] | Ego |
| [AGD20K](https://arxiv.org/abs/2203.09905) | 2022 | CVPR | [[Code](https://github.com/lhc1224/Cross-View-AG)] [[Page](https://opendatalab.com/OpenDataLab/AGD20K)] | Ego+Exo |
| [EgoHOS](https://arxiv.org/abs/2208.03826) | 2022 | ECCV | [[Code](https://github.com/owenzlz/EgoHOS)] [[Page](https://www.seas.upenn.edu/~shzhou2/projects/eos_dataset/)] | Ego |
| [DexYCB](https://arxiv.org/abs/2104.04631) | 2021 | CVPR | [[Code](https://github.com/NVlabs/dex-ycb-toolkit)] [[Page](https://dex-ycb.github.io/)] | Exo |
| [H2O](https://arxiv.org/abs/2104.11181) | 2021 | ICCV | [[Code](https://github.com/taeinkwon/h2odataset)] [[Page](https://taeinkwon.com/projects/h2o/)] | Ego |
| [MOW](https://arxiv.org/abs/2012.09856) | 2021 | ICCV | [[Code](https://github.com/ZheC/MOW)] [[Page](https://zhec.github.io/rhoi/)] | Exo |
| [100DOH](https://arxiv.org/abs/2006.06669) | 2020 | CVPR | [[Code](https://github.com/ddshan/hand_object_detector)] [[Page](https://fouheylab.eecs.umich.edu/~dandans/projects/100DOH/)] | Ego+Exo |
| [Kinetics-700](https://arxiv.org/abs/2010.10864) | 2020 | arXiv 2020.10 | [[Code](https://github.com/cvdfoundation/kinetics-dataset)] [[Page](https://huggingface.co/datasets/bitmind/Kinetics-700)] | Exo |
| [HowTo100M](https://arxiv.org/abs/1906.03327) | 2019 | ICCV | [[Code](https://github.com/antoine77340/howto100m)] [[Page](https://www.di.ens.fr/willow/research/howto100m/)] | Ego+Exo |
| [FreiHAND](https://arxiv.org/abs/1909.04349) | 2019 | ICCV | [[Code](https://github.com/lmb-freiburg/freihand)] [[Page](https://lmb.informatik.uni-freiburg.de/projects/freihand/)] | Exo |
| [FPHA](https://arxiv.org/abs/1704.02463) | 2018 | CVPR | [[Code](https://github.com/guiggh/hand_pose_action)] [[Page](https://kcvl-kaist.github.io/FPHA/)] | Ego |
| [VLOG](https://arxiv.org/abs/1712.02310) | 2018 | CVPR | [[Code](https://github.com/dfouhey/VLOGToolkit)] [[Page](https://cs.nyu.edu/~fouhey/2017/VLOG/index.html)] | Exo |
| [EPIC-KITCHENS](https://arxiv.org/abs/1804.02748) | 2018 | ECCV | [[Code](https://github.com/epic-kitchens/epic-kitchens-55-annotations)] [[Page](https://epic-kitchens.github.io/)] | Ego |
| [EGTEA Gaze+](https://openaccess.thecvf.com/content_ECCV_2018/papers/Yin_Li_In_the_Eye_ECCV_2018_paper.pdf) | 2018 | ECCV | [[Code](https://github.com/amitsou/EGTEA_Gaze_Plus_Downloader)] [[Page](http://cbi.gatech.edu/fpv)] | Ego |
| [YouCook2](https://arxiv.org/abs/1703.09788) | 2018 | AAAI | [[Code](https://github.com/LuoweiZhou/ProcNets-YouCook2)] [[Page](http://youcook2.eecs.umich.edu/)] | Exo |
| [Something-Something](https://arxiv.org/abs/1706.04320) | 2017 | ICCV | [[Code](https://huggingface.co/datasets/HuggingFaceM4/something_something_v2)] [[Page](https://twentybn.com/datasets/something-something)] | Exo |
| [Charades](https://arxiv.org/abs/1604.01753) | 2016 | ECCV | [[Code](https://github.com/xiaolonw/CharadesDet)] [[Page](https://leooo-huang.github.io/awesome-human-activity-recognition/datasets/multimodal/charades/)] | Exo |
| [ActivityNet](https://openaccess.thecvf.com/content_cvpr_2015/papers/Heilbron_ActivityNet_A_Large-Scale_2015_CVPR_paper.pdf) | 2015 | CVPR | [[Code](https://github.com/activitynet/ActivityNet)] [[Page](http://activity-net.org/)] | Exo |
| [EgoHands](https://ieeexplore.ieee.org/document/7410583) | 2015 | ICCV | [[Code](https://github.com/victordibia/handtracking)] [Page] | Ego |
| [Breakfast](https://openaccess.thecvf.com/content_cvpr_2014/papers/Kuehne_The_Language_of_2014_CVPR_paper.pdf) | 2014 | CVPR | [Code] [[Page](https://durandtibo.github.io/aroma/datasets/breakfast/)] | Exo |


### Human Video Generation
This section summarizes works that use video generation techniques to synthesize human videos for robot learning.

#### 2026
- 🌟🤖 [[ICLR](https://arxiv.org/abs/2507.00990)] Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations [[Code](https://github.com/shivanshpatel35/rigvid)] [[Page](https://rigvid-robot.github.io/)]
- 🌟 [[CVPR](https://arxiv.org/abs/2512.17907)] Dexterous World Models [[Code](https://github.com/snuvclab/dwm)] [[Page](https://snuvclab.github.io/dwm/)] 
- 🌟🤖 [[ICRA](https://arxiv.org/abs/2510.08568)] NovaFlow: Zero-Shot Manipulation via Actionable Flow from Generated Videos [[Code](https://github.com/rai-opensource/NovaFlow)] [[Page](https://novaflow.lhy.xyz/)]

#### 2025

- 🌟🤖 [[CoRL](https://arxiv.org/abs/2406.16862)] Dreamitate: Real-World Visuomotor Policy Learning via Video Generation [[Code](https://github.com/cvlab-columbia/dreamitate)] [[Page](https://dreamitate.cs.columbia.edu/)]
- 🌟🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.15840)] Large Video Planner Enables Generalizable Robot Control [[Code](https://github.com/buoyancy99/large-video-planner)] [[Page](https://www.boyuan.space/large-video-planner/)]
- 🌟🤖 [[arXiv 2025.12](https://arxiv.org/abs/2512.24766)] Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow [[Code](https://github.com/KDharmarajanDev/Dream2Flow/)] [[Page](https://dream2flow.github.io/)]


#### 2024

- 🤖 [[arXiv 2024.09](https://arxiv.org/abs/2409.16283)] Gen2Act: Human Video Generation in Novel Scenarios Enables Generalizable Robot Manipulation [Code] [[Page](https://homangab.github.io/gen2act/)]

#### 2023
- 🌟 [[NeurIPS](https://arxiv.org/abs/2302.00111)] Learning Universal Policies via Text-Guided Video Generation [[Code](https://github.com/flow-diffusion/AVDC)] [[Page](https://universal-policy.github.io/unipi/)]

#### 2020

- 🤖 [[RA-L](https://doi.org/10.1109/LRA.2020.2977835)] Learning One-Shot Imitation from Humans Without Humans [Code] [[Page](https://sites.google.com/view/tecnets-humans)]


### HOI Analysis Techniques
This section gathers HOI analysis techniques, including hand/object detection and reconstruction, pose estimation, and point tracking tools widely used in LfHV research.

#### 2026

- 🌟 [[arXiv 2026.02](https://arxiv.org/abs/2602.15989)] SAM 3D Body: Robust Full-Body Human Mesh Recovery [[Code](https://github.com/facebookresearch/sam-3d-body)] [[Page](https://ai.meta.com/blog/sam-3d/)]

#### 2025

- 🌟 [[CVPR](https://arxiv.org/abs/2409.12259)] WiLoR: End-to-End 3D Hand Localization and Reconstruction In-the-Wild [[Code](https://github.com/rolpotamias/WiLoR)] [[Page](https://rolpotamias.github.io/WiLoR/)]
- 🌟 [[CVPR](https://arxiv.org/abs/2501.02973)] HaWoR: World-Space Hand Motion Reconstruction from Egocentric Videos [[Code](https://github.com/ThunderVVV/HaWoR)] [[Page](https://hawor-project.github.io/)]
- 🌟 [[CVPR](https://arxiv.org/abs/2503.18673)] Any6D: Model-Free 6D Pose Estimation of Novel Objects [[Code](https://github.com/taeyeopl/Any6D)] [[Page](https://sites.google.com/view/taeyeop-lee/any6d)]
- 🌟 [[CVPR](https://arxiv.org/abs/2412.01506)] Structured 3D Latents for Scalable and Versatile 3D Generation [[Code](https://github.com/Microsoft/TRELLIS)] [[Page](https://microsoft.github.io/TRELLIS/)]
- 🌟 [[ICCV](https://arxiv.org/abs/2410.11831)] CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos [[Code](https://github.com/facebookresearch/co-tracker)] [[Page](https://cotracker3.github.io/)]
- 🌟 [[ICCV](https://arxiv.org/abs/2507.12462)] SpatialTrackerV2: Advancing 3D Point Tracking with Explicit Camera Motion [[Code](https://github.com/henry123-boy/SpaTrackerV2)] [[Page](https://spatialtracker.github.io/)]
- [[Meshy AI](https://www.meshy.ai/)] Meshy AI: The #1 AI 3D Model Generator for Creators [[Page](https://www.meshy.ai/)] 

#### 2024

- 🌟 [[CVPR](https://arxiv.org/abs/2312.05251)] Reconstructing Hands in 3D with Transformers [[Code](https://github.com/geopavlakos/hamer)] [[Page](https://geopavlakos.github.io/hamer/)]
- 🌟 [[CVPR](https://arxiv.org/abs/2312.08344)] FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects [[Code](https://github.com/NVlabs/FoundationPose)] [[Page](https://nvlabs.github.io/FoundationPose/)]
- 🌟 [[CVPR](https://arxiv.org/abs/2404.04319)] SpatialTracker: Tracking Any 2D Pixels in 3D Space [[Code](https://github.com/henry123-boy/SpaTracker)] [[Page](https://henry123-boy.github.io/SpaTracker/)]
- 🌟 [[ECCV](https://arxiv.org/abs/2307.07635)] CoTracker: It Is Better to Track Together [[Code](https://github.com/facebookresearch/co-tracker)] [[Page](https://co-tracker.github.io/)]
- 🌟 [[ECCV](https://arxiv.org/abs/2407.15420)] Local All-Pair Correspondence for Point Tracking [[Code](https://github.com/cvlab-kaist/locotrack)] [[Page](https://ku-cvlab.github.io/locotrack/)]
- 🌟 [[ACCV](https://arxiv.org/abs/2402.00847)] Bootstap: Bootstrapped Training for Tracking-Any-Point [[Code](https://github.com/google-deepmind/tapnet?tab=readme-ov-file#checkpoints)] [[Page](https://bootstap.github.io/)]
- 🌟 [[arXiv 2024.04](https://arxiv.org/abs/2404.07191)] InstantMesh: Efficient 3D Mesh Generation from a Single Image with Sparse-View Large Reconstruction Models [[Code](https://github.com/TencentARC/InstantMesh)] [[Page](https://huggingface.co/spaces/TencentARC/InstantMesh)]

#### 2023

- 🌟 [[NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/hash/612a7948f3294a02a63d970566ca8536-Abstract-Conference.html)] Towards a Richer 2D Understanding of Hands at Scale [[Code](https://github.com/EvaCheng-cty/hands23_detector)] [Page]
- 🌟 [[CVPR](https://arxiv.org/abs/2303.14158)] BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects [[Code](https://github.com/NVlabs/BundleSDF)] [[Page](https://bundlesdf.github.io/)]
- 🌟 [[ICCV](https://arxiv.org/abs/2306.08637)] TAPIR: Tracking Any Point with Per-Frame Initialization and Temporal Refinement [[Code](https://github.com/google-deepmind/tapnet)] [[Page](https://deepmind-tapir.github.io/)]


#### 2022
- 🌟 [[CVPR](https://arxiv.org/abs/2112.09120)] Human Hands as Probes for Interactive Object Understanding [[Code](https://github.com/uiuc-robovision/hands-as-probes)] [[Page](https://s-gupta.github.io/hands-as-probes/)]
- [[CoRL](https://arxiv.org/abs/2212.06870)] MegaPose: 6D Pose Estimation of Novel Objects via Render & Compare [Code[https://github.com/megapose6d/megapose6d]] [Page[https://megapose6d.github.io/]]
- 🌟 [[ICCVW](https://arxiv.org/abs/2008.08324)] FrankMocap: Fast Monocular 3D Hand and Body Motion Capture by Regression and Integration [[Code](https://github.com/facebookresearch/frankmocap)] [[Page](https://github.com/facebookresearch/frankmocap)]


#### 2020

- 🌟 [[CVPR](https://arxiv.org/abs/2006.06669)] Understanding Human Hands in Contact at Internet Scale [[Code](https://github.com/ddshan/hand_object_detector)] [[Page](https://fouheylab.eecs.umich.edu/~dandans/projects/100DOH/)]
- 🌟 [[CVPRW](https://arxiv.org/abs/2006.10214)] MediaPipe Hands: On-Device Real-Time Hand Tracking [[Code](https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/hands.md)] [[Page](https://ai.google.dev/edge/mediapipe/solutions/guide?hl=zh-cn)]

> Other vision foundation models like Grounding DINO, YOLO series, SAM series are also widely used in the LfHV literature.

## LICENSE
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.




## Contact
If you have any questions or suggestions, please feel free to contact [Junyi Ma](mailto:junyi.ma@sjtu.edu.cn).
