poplist_path='./poplist.txt'
out_path='./PCAplot.r'
poptext = open(poplist_path).readlines()
pca = open(out_path,'w')
pop_list=[]
pca.writelines("""data=read.table("")
pop=data[,12]
ind=data[,1]
PC1=data[,2]
PC2=data[,4]
PC3=data[,4]
#layout(matrix(c(1,2,3,4),2,2),widths=c(1,1),heights=c(1,1))
layout(matrix(c(1,2)),widths=c(2,1),heights=c(3,1))
par(mar=c(2.1,2,0,0.3))
plot(PC1,PC2,type="n",cex.axis=0.5,cex.lab=1,cex.main=1,mgp=c(1,0.1,0), tck=-0.005)
#par(mar = c(4, 4, 1, 0.5), bg = "yellow")   # 设置边距参数和背景色
#par(pin=c(2,3))   #定义图形为2英寸宽，3英寸高
#par(lwd=2,cex=1.5)   #线条为默认的2倍宽，符号为默认的1.5倍
#par(cex.axis=0.75,font.axis=3)   #坐标轴文字缩放为原来的75%，斜体
frame=data.frame(PC1=PC1,PC2=PC2,name=pop,region=pop)
to21=c("#EE0000","#B0C4DE","#1E90FF","#87CEFA","#00FFFF","#808000","#ADD8E6","#D2691E","#FFC0CB","#FF69B4","#EE82EE","#BA55D3","#8A2BE2","#0000CD","#000080","#F4A460","#FFF5EE","#FF7F50","#FF6347","#2F4F4F","#48D1CC","#7FFFAA","#8FBC8F","#228B22","#7FFF00","#556B2F","#FFFFF0","#FDF5E6","#FFA500","#FFDEAD","#DEB887","#FAF0E6","#8D5223","#6F96F2","#00CD66","#ABF4DC","#F88BD5","#AB82FF","#FFC534","#3787B4","#FFDAB9","#6B8E23","#FF8C69","#2B2B2C","#D02090","#FF1493","#20B2AA","#708090","#FFFAFA","#CD5C5C","#B22222","#FFFFFF","#808080","#D3D3D3","#F0FFFF","#C0C0C0","#F5FFFA","#F0FFF0","#E6E6FA")
#59 gray
########################
########################
""")
j=-1
for i in poptext:
    i=i.strip()
    if i[0] == '=':
        j+=1
        pop_list.append([])
        pop_list[j].append(i.strip("="))
    else:
        pop_list[j].append(i)
for i in range(0,len(pop_list)):
    pca.writelines("".join("".join(pop_list[i][0].split(sep="-")).split())+'_col=to21['+str(i+1)+']\n')
for i in pop_list:
    pca.writelines('# '+i[0]+'\n')
    for j in range(1, len(i)):
        pca.writelines('reg="'+i[j]+'"\n')
        pca.writelines('points(subset(frame,region==reg)$PC1,subset(frame,region==reg)$PC2,pch={},bg={}_col,col={}_col,cex=0.6)\n'.format(str(j-1),"".join("".join(i[0].split(sep="-")).split()),"".join("".join(i[0].split(sep="-")).split())))
pca.writelines("########################\n########################\n# legend\npar(mar=c(5,1,0,2))\nplot.new()\n")
# pops
pops=[]
for i in pop_list:
    pops.append('","'.join(i))
pops='"'+'","'.join(pops)+'"'
pca.writelines('pops=   c({})\n'.format(pops))
# cols,borders,symb,fonts
cols=[]
symb=[]
fonts=[]
for i in pop_list:
    cols.append('NA')
    symb.append('NA')
    fonts.append('2')
    for j in range(len(i)-1):
        cols.append("".join("".join(i[0].split(sep="-")).split())+"_col")
        symb.append(str(j))
        fonts.append(str(1))
cols = ",".join(cols)
symb = ",".join(symb)
fonts = ",".join(fonts)
# print(cols)
# print(symb)
# print(fonts)
pca.writelines('cols=   c({})\n'.format(cols))
pca.writelines('borders=c({})\n'.format(cols))
pca.writelines('symb=   c({})\n'.format(symb))
pca.writelines('fonts=  c({})\n'.format(fonts))
pca.writelines('legend("top",pops,pch=symb,pt.bg=cols,col=borders,ncol=7,cex=0.3,pt.cex=0.4,bty="o",text.font=fonts,xpd=TRUE)')