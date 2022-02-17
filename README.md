# Pioneer P3dx Model

Um modelo ROS/CoppeliaSim do Pioneer 3DX adaptado por Davi Juvêncio (davi.j.g.sousa@ee.ufcg.edu.br).

# Para instalar:

```
$ mkdir -p <catkin_ws>/src
$ cd <catkin_ws>/src
$ git clone https://github.com/davijuvencio/eRobotica_P3dx_CoppeliaSim.git
$ cd ..
$ catkin_make
```

# Para usar:

```
Source o seu espaço de trabalho
$ source devel/setup.bash
Configure o launch com os diretórios de instalação do coppeliasim e de sua cena de simulação
$ gedit src/eRobotica_P3dx_CoppeliaSim/p3dx_coppeliasim/launch/simulation.launch
No editor de texto, configurando a cena:
$ <arg name="scene" default="$(find p3dx_coppeliasim)/scene/<sua_cena>.ttt"/>
No editor de texto, configurando o diretório de instalação do coppeliasim:
$ <arg name="COPPELIA_PATH" default="<seu_diretorio_de_instalação_do_coppeliasim>"/>
Rodando o pacote
$ roslaunch p3dx_coppeliasim simulation.launch
```
