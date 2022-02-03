""" El problema consiste en crear una lista dinámica en HTML (ul-li)
"""
#Código sin patrón de diseño: BUILDER

palabras = ['Rojo','Verde','Azul']
html = ['<ul>']

for p in palabras:
    html.append(f'<li>{p}</li>')
html.append('</ul>')
print('\n'.join(html)) #imprimir HTML

#Patron de diseño: BUILDER
class HtmlElement:

    def __init__(self,tag="",text=""):
        self.tag = tag
        self.text = text
        self.elementos = []
    
    def html(self):
        lineas = []
        
        if self.text: #li
            lineas.append(f' <{self.tag}>{self.text}</{self.tag}>')
        else: #ul
            lineas.append(f'<{self.tag}>')
                
        for e in self.elementos: #recursividad 
            lineas.append(e.html())
        
        if not self.text: #fin ul
            lineas.append(f'<{self.tag}>')
        
        return '\n'.join(lineas)
    
    def __str__(self): #imprimir el mismo objeto
        return self.html()
    
    @staticmethod
    def crear(tag):
        return HtmlBuilder(tag)
    
class HtmlBuilder:
    padre = HtmlElement()

    def __init__(self, tag): #tag = ul
        self.tag = tag
        self.padre.tag = tag

    # no instanciado
    def agregar_li(self, tag_hijo, text_hijo):
        self.padre.elementos.append(
            HtmlElement(tag_hijo, text_hijo)
        )

    # misma instancia
    def agregar_li_self(self, tag_hijo, text_hijo):
        self.padre.elementos.append(
            HtmlElement(tag_hijo, text_hijo)
        )
        return self

    def clear(self):
        self.padre = HtmlElement(tag=self.tag)

    def __str__(self):
        return str(self.padre)

#Patron de diseño de forma ordinaria (tradicional)

print('\n\n Builder #1: \n')

builder = HtmlElement.crear('ul')
builder.agregar_li('li', 'Rojo')
builder.agregar_li('li', 'Verde')
builder.agregar_li('li', 'Azul')
print(builder)

#Patron de diseño de forma multiple función

print('\n\n Builder #2: \n')
builder.clear()
builder.agregar_li_self('li', 'Rojo') \
        .agregar_li_self('li', 'Verde') \
        .agregar_li_self('li', 'Azul')

print(builder)
