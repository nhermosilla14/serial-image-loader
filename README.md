# Serial Image Loader GUI
*************************
## EN

A note on modifications and hacks.
----------------------------------

It's possible (and, in fact, very easy) to modify everything inside this program. The license under which it's released is GPLv3 or higher, so modding and sharing is encouraged, that is in part the purpose.

To change the interface, a basic Python knowledge is required. Ideally it's also useful to understand something about object oriented programming, but nothing you can't learn with a bit of help from Youtube. The interface was made using QtDesigner, which allows to build windows and interfaces through the use of a mouse, dragging layouts, buttons, etc. The .ui file should be modified using that software, it's recommended to use the Qt5 version. It's possible to import the ui file directly from within the code, however it's also feasible to compile it in order to transform it into a common Qt5 class, using pyuic. That's what I did originally.

## ES

Una nota sobre modificaciones y hacks.
--------------------------------------

Es posible (y de hecho muy sencillo) modificar todo de este programa. La licencia bajo la cual está hecho es la GPLv3 o superior, por lo que se recomienda modificarlo y compartirlo, pues es en parte la idea. 

Para cambiar la interfaz, un conocimiento básico de Python es requerido. Idealmente también es bueno entender algo sobre programación orientada a objetos, pero nada que no se pueda solventar con un poco de Youtube. La interfaz fue hecha usando QtDesigner, que permite crear ventanas e interfaces mediante el uso de mouse, arrastrando layouts, botones, etc. El archivo .ui se modifica con dicho software, idealmente sobre la versión para Qt5. Es posible importar directamente el archivo de la ui, sin embargo se puede igualmente compilar para transformar la interfaz diseñada en una clase común de Qt5, usando pyuic. Es lo que se ha usado para el desarrollo original de la interfaz.
