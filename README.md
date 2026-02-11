# 2-Dimensionality-analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

本项目集合了群体遗传学中常用的**降维分析（Dimensionality Reduction）**脚本与可视化工具，涵盖了从数据处理到结果展示的全流程。

## 📊 包含的分析模块

仓库内的脚本和工具按以下逻辑组织，涵盖了目前主流的群体结构分析方法：

1. **基础降维与计算**:
   * **PLINK**: 经典的 PCA 与相关性计算。
   * **Scikit-learn**: 基于 Python 的机器学习降维框架。
   * **MDS 计算**: 包含 `2-计算MDS.r` 等多维尺度分析脚本。

2. **可视化与进阶分析**:
   * **PCA 可视化**: 二维/三维主成分分析绘图。
   * **DAPC**: 判别分析主成分分析。
   * **UMAP**: 用于展示更复杂群体结构的非线性降维。
   * **PCoA 可视化**: 基于距离矩阵的主坐标分析。
   * **CA 关联分析**: 对应分析与相关性研究。

## 🛠️ 技术栈
* **数据处理**: PLINK, Python (Pandas/NumPy)
* **统计分析**: R (adegenet, ape), Scikit-learn
* **绘图展示**: ggplot2, Matplotlib, Seaborn

## 🚀 快速使用
你可以根据分析需求，进入对应的子目录寻找脚本。大部分 R 脚本支持直接在 RStudio 中运行，Python 脚本建议在 Conda 环境下执行。
