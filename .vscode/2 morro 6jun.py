
class constructor:
 def _init_(self,nombre):
    self.nombre=nombre
    def construir(self):
        print(self.nombre, "esta preparando los planos generales")
#clases hijas:casa departamento,bodega
class casa(constructor):
 def _init_(self,nombre,piso,baño):
    self.nombre=nombre
    self.piso=piso
    self.baño=baño
    def construir(self):
        print(self.nombre, "esta construyendo el piso")
        print(self.nombre, "esta construyendo el baño")
        class departamento(constructor):
            def _init_(self,nombre,piso,baño):
                self.nombre=nombre
                self.piso=piso
                self.baño=baño
                def construir(self):
                    print(self.nombre, "esta construyendo el piso")
                    print(self.nombre, "esta construyendo el baño")
                    class bodega(constructor):
                        def _init_(self,nombre,piso,baño):
                            self.nombre=nombre
                            self.piso=piso
                            self.baño=baño
                            def construir(self):
                                print(self.nombre, "esta construyendo el piso")
                                print(self.nombre, "esta construyendo el baño")
                                print(self.nombre, "esta preparando los planos generales")

#principal(recordar indentar)
#esto es instanciar ycorrer los metodos ,usando abstraccion ,acompañando de dos lineas donde creo el metodo y donde mando a llamar el metodo

casa=casa("casa de la bodega","piso de la casa","baño de la casa")
casa.construir()
casa.construir()
departamento=departamento("departamento de la casa","piso de la departamento","baño de la departamento") # type: ignore
departamento.construir()
departamento.construir()
   