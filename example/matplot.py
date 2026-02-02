
import numpy as np
import matplotlib.pyplot as plt


rng = np.random.default_rng(42)
# 生成数据
x = np.linspace(0, 2 * np.pi, 200)
# 生成三组数据
group1 = [np.sin(x) + 0.1 * rng.standard_normal(x.size)]
group2 = [np.sin(x + 0.6) + 0.1 * rng.standard_normal(x.size)]
group3 = [np.sin(x + 1.2) + 0.1 * rng.standard_normal(x.size)]
# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
ax.plot(x, group1[0], label="group1", color="#1f77b4", linewidth=2, marker="o", markersize=3, markevery=10)# 绘制group1
ax.plot(x, group2[0], label="group2", color="#ff7f0e", linewidth=2, marker="s", markersize=3, markevery=10)# 绘制group2
ax.plot(x, group3[0], label="group3", color="#315531", linewidth=2, marker="^", markersize=3, markevery=10)# 绘制group3
# 设置标题和标签
ax.set_title("Sine Series with Noise", fontsize=14, pad=12)
ax.set_xlabel("Angle (radians)", fontsize=12)
ax.set_ylabel("Amplitude", fontsize=12)
# 设置坐标轴范围和刻度
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
# 设置x轴刻度
ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
# 添加网格和图例
ax.grid(True, which="major", linestyle="--", alpha=0.4)
# 开启次刻度
ax.minorticks_on()
ax.grid(True, which="minor", linestyle=":", alpha=0.2)
# 添加图例
ax.legend(loc="upper right", frameon=True, fancybox=True, framealpha=0.9)
# 设置背景颜色
ax.set_facecolor("#f8f9fb")
# 调整布局并保存图像
fig.tight_layout()
# 保存图像
#fig.savefig("sine_groups.png", dpi=200)
plt.show()

