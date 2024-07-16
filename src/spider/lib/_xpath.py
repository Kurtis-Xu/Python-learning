from lxml import etree

xml = '''
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>xxx</nick>
        </div>
    </author>

    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
'''

tree = etree.XML(xml)
print(tree.xpath('/book/author/nick/text()'))  # text() 获取节点中的文本
print(tree.xpath('/book/author//nick/text()'))  # 获取后代，相当于 css 选择器中的空格
print(tree.xpath('/book/author/*/nick/text()'))  # * 通配符
print(tree.xpath('/book/author/nick[@class="joy"]/text()'))  # @ 通过属性查找

print(list(map(lambda nick: nick.xpath('./text()'), tree.xpath('/book/author/nick'))))
