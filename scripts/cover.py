import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(5.6, 2.8), facecolor='#1a1a2e')
ax.set_xlim(0, 560)
ax.set_ylim(0, 280)
ax.axis('off')

# Background
ax.add_patch(mpatches.Rectangle((0, 0), 560, 280, color='#1a1a2e'))

# Title
ax.text(280, 200, 'Triagegeist', fontsize=28, fontweight='bold',
        color='white', ha='center', va='center', fontfamily='monospace')

ax.text(280, 163, 'Acuity Prediction & Demographic Bias Audit',
        fontsize=10, color='#a8dadc', ha='center', va='center')

# Divider line
ax.plot([80, 480], [130, 130], color='#457b9d', linewidth=0.5, alpha=0.5)

# Stats
ax.text(140, 100, '85.9%', fontsize=22, fontweight='bold',
        color='#e63946', ha='center', va='center')
ax.text(140, 75, 'Validation Accuracy', fontsize=7,
        color='#a8dadc', ha='center', va='center')

ax.text(280, 100, '5.27%', fontsize=22, fontweight='bold',
        color='#e63946', ha='center', va='center')
ax.text(280, 75, 'Undertriage Rate', fontsize=7,
        color='#a8dadc', ha='center', va='center')

ax.text(420, 100, '7.2%', fontsize=22, fontweight='bold',
        color='#e63946', ha='center', va='center')
ax.text(420, 75, 'Highest Risk Group', fontsize=7,
        color='#a8dadc', ha='center', va='center')

# Footer
ax.text(280, 30, 'Laitinen-Fredriksson Foundation · Triagegeist Competition 2026',
        fontsize=7, color='#457b9d', ha='center', va='center')

plt.tight_layout(pad=0)
plt.savefig(r'C:\Users\16315\Desktop\Python\Projects\Triage Project\outputs\cover_image.png',
            dpi=100, bbox_inches='tight', facecolor='#1a1a2e')
plt.show()
print("Cover image saved.")