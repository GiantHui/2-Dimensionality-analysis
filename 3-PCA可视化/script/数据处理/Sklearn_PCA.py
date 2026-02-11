import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, Isomap, LocallyLinearEmbedding

# 加载数据
file_path = '/mnt/c/Users/Administrator/Desktop/6级_ref.csv'
data = pd.read_csv(file_path)
pca_data = data.drop(columns=data.columns[0])

# 执行PCA
pca = PCA(n_components=2)
pca_results = pca.fit_transform(pca_data.T)  # T表示转置
explained_variance_ratio = pca.explained_variance_ratio_
with open('/mnt/c/Users/Administrator/Desktop/PCA降维结果解释度.txt', 'w') as f:
    # 将解释度写入文件
    f.write('Explained Variance Ratio:\n')
    for i, ratio in enumerate(explained_variance_ratio):
        f.write(f'Component {i+1}: {ratio:.4f}\n')
    f.write('\n')


# 将结果写入新的csv文件
results_df = pd.DataFrame({
    'PCA1': pca_results[:, 0],
    'PCA2': pca_results[:, 1],
    'Ethnic Group': pca_data.columns
})
results_df.to_csv('/mnt/c/Users/Administrator/Desktop/PCA降维结果.csv', index=False)
# 执行t-SNE
# 注意，在使用这个方法前请明确参数的含义！！
tsne = TSNE(n_components=2, perplexity=20, learning_rate=200, random_state=42)
tsne_results = tsne.fit_transform(pca_data.T)
# 将结果写入新的csv文件
results_df = pd.DataFrame({
    't-SNE1': tsne_results[:, 0],
    't-SNE2': tsne_results[:, 1],
    'Ethnic Group': pca_data.columns
})
results_df.to_csv('/mnt/c/Users/Administrator/Desktop/t-SNE降维结果.csv', index=False)

# 执行Isomap
isomap = Isomap(n_components=2, n_neighbors=5)
isomap_results = isomap.fit_transform(pca_data.T)
# 将结果写入新的csv文件
results_df = pd.DataFrame({
    'isomap1': isomap_results[:, 0],
    'isomap2': isomap_results[:, 1],
    'Ethnic Group': pca_data.columns
})
results_df.to_csv('/mnt/c/Users/Administrator/Desktop/isomap降维结果.csv', index=False)

# 执行LLE
# 注意，在使用这个方法前请明确参数的含义！！
lle = LocallyLinearEmbedding(n_components=2, n_neighbors=10, method='standard')
lle_results = lle.fit_transform(pca_data.T)
# 将结果写入新的csv文件
results_df = pd.DataFrame({
    'lle1': lle_results[:, 0],
    'lle2': lle_results[:, 1],
    'Ethnic Group': pca_data.columns
})
results_df.to_csv('/mnt/c/Users/Administrator/Desktop/lle降维结果.csv', index=False)

# 准备结果数据
results_df = pd.DataFrame({
    'PCA1': pca_results[:, 0],
    'PCA2': pca_results[:, 1],
    't-SNE1': tsne_results[:, 0],
    't-SNE2': tsne_results[:, 1],
    'Isomap1': isomap_results[:, 0],
    'Isomap2': isomap_results[:, 1],
    'LLE1': lle_results[:, 0],
    'LLE2': lle_results[:, 1],
    'Ethnic Group': pca_data.columns
})

# 可视化
plt.figure(figsize=(24, 12))
for i, (label, comp1, comp2) in enumerate(zip(['PCA', 't-SNE', 'Isomap', 'LLE'], 
                                             ['PCA1', 't-SNE1', 'Isomap1', 'LLE1'], 
                                             ['PCA2', 't-SNE2', 'Isomap2', 'LLE2'])):
    plt.subplot(2, 2, i+1)
    sns.scatterplot(x=comp1, y=comp2, hue='Ethnic Group', data=results_df, palette='viridis')
    plt.title(f'{label} Visualization of Ethnic Groups')
    plt.xlabel(f'{label} 1')
    plt.ylabel(f'{label} 2')
    plt.legend([],[], frameon=False)  # 隐藏图例以节省空间

plt.tight_layout()
plt.show()