# ==== 加载需要的基础包 ====
# 其实本段代码用不到额外包，base R足够，ggplot2用于可视化时才用，这里省略。

# ==== 设置工作目录 ====
setwd("E:/OneDrive/Y-chromosome/Affy/MDS（PCoA）/")

# ==== 读取FST矩阵 ====
fst_matrix <- as.matrix(read.csv("FST值矩阵.csv", row.names = 1, check.names = FALSE))

# ==== 检查矩阵 ====
if (!is.numeric(fst_matrix)) stop("FST矩阵中含有非数值型元素")
if (!all(fst_matrix == t(fst_matrix))) warning("FST矩阵可能不对称")

# ==== 运行PCoA ====
# 使用欧氏距离的度量，可以直接传入dist对象
pcoa_result <- cmdscale(as.dist(fst_matrix), k = nrow(fst_matrix) - 1, eig = TRUE)

# ==== 计算解释比例（只用正特征值） ====
positive_eig <- pcoa_result$eig[pcoa_result$eig > 0]
variance_explained <- round(positive_eig / sum(positive_eig) * 100, 2)

# ==== 提取前两主坐标 ====
pcoa_coords <- pcoa_result$points[, 1:2]
colnames(pcoa_coords) <- c("PCo1", "PCo2")

# ==== 输出PCoA坐标到CSV ====
write.csv(pcoa_coords, file = "pcoa_coordinates-1.csv", quote = FALSE)

# ==== 输出解释比例到TXT ====
variance_text <- paste0("PCoA1解释的方差百分比: ", variance_explained[1], "%\n",
                        "PCoA2解释的方差百分比: ", variance_explained[2], "%\n")
writeLines(variance_text, con = "pcoa_variance_explained-1.txt")

# ==== 打印在控制台上，方便查看 ====
cat(variance_text)

# ==== 完成 ====
cat("PCoA分析完成，结果已保存到 pcoa_coordinates-1.csv 和 pcoa_variance_explained-1.txt\n")

