import xml.etree.ElementTree as ET

# 创建 SVG 命名空间
svg_namespace = "http://www.w3.org/2000/svg"

# 解析 SVG 文件
tree = ET.parse('svgtest.svg')
root = tree.getroot()

# 找到要查找位置的元素
target_elem = root.find('{%s}rect' % svg_namespace)
print(target_elem)

# 找到该元素的父元素
#parent_elem = target_elem.getparent()

for position, elem in enumerate(root):
    if elem is target_elem:
        break

circle_elem = ET.Element('circle')
circle_elem.set('cx', '150')
circle_elem.set('cy', '100')
circle_elem.set('r', '50')
circle_elem.set('fill', 'red')

# 在矩形元素后面插入圆元素
root.insert(position + 1, circle_elem)
ET.register_namespace('', 'http://www.w3.org/2000/svg')

# 将修改后的 XML 树写入文件
tree.write('modified_example.svg')

