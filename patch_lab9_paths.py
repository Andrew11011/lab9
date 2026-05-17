from pathlib import Path

p = Path(r'c:\Users\andze\OneDrive\Desktop\Computer Science\numerical methods\lab9\lab9_hooke_jeeves.ipynb')
text = p.read_text(encoding='utf-8')
replacements = {
    "import numpy as np\nimport matplotlib.pyplot as plt\nfrom matplotlib import cm\nimport warnings\nwarnings.filterwarnings('ignore')\n\nprint(\"Бібліотеки імпортовано успішно\")":
    "import numpy as np\nimport os\nimport matplotlib.pyplot as plt\nfrom matplotlib import cm\nimport warnings\nwarnings.filterwarnings('ignore')\nos.makedirs('outputs', exist_ok=True)\n\nprint(\"Бібліотеки імпортовано успішно\")",
    "plt.savefig('/mnt/user-data/outputs/rosenbrock_trajectory.png', dpi=120)":
    "plt.savefig('outputs/rosenbrock_trajectory.png', dpi=120)",
    "plt.savefig('/mnt/user-data/outputs/system_equations.png', dpi=120)":
    "plt.savefig('outputs/system_equations.png', dpi=120)",
    "plt.savefig('/mnt/user-data/outputs/target_function_descent.png', dpi=120, bbox_inches='tight')":
    "plt.savefig('outputs/target_function_descent.png', dpi=120, bbox_inches='tight')",
    "with open('/mnt/user-data/outputs/trajectory.txt', 'w', encoding='utf-8') as f:":
    "with open('outputs/trajectory.txt', 'w', encoding='utf-8') as f:",
}
for old, new in replacements.items():
    if old not in text:
        raise ValueError(f'Missing exact match: {old[:80]}')
    text = text.replace(old, new)
p.write_text(text, encoding='utf-8')
print('patched successfully')
