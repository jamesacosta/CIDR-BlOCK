CIDR son las siglas de "Classless Inter-Domain Routing" (en español, enrutamiento interdominio sin clases). 
Un CIDR block, o bloque CIDR, es una notación que se utiliza en redes de computadoras para representar
un rango de direcciones IP de manera compacta y eficiente.

En el pasado, las direcciones IP se dividían en clases (Clase A, Clase B, Clase C, etc.), y cada clase tenía un tamaño 
de prefijo de red fijo. Sin embargo, con el crecimiento de Internet, esta estructura se volvió poco práctica ya que 
desperdiciaba muchas direcciones IP. CIDR fue diseñado para superar esta limitación al permitir la asignación de 
direcciones IP en bloques de diferentes tamaños, lo que proporciona una mayor flexibilidad en la asignación de 
direcciones IP.

Un bloque CIDR se representa mediante una dirección IP de red seguida de una barra "/" y un número que indica 
la cantidad de bits utilizados para la máscara de red. Por ejemplo, "192.168.0.0/24" representa un bloque CIDR que 
incluye todas las direcciones IP desde 192.168.0.0 hasta 192.168.0.255, donde los primeros 24 bits son la parte de 
red y los últimos 8 bits son la parte de host.

En resumen, CIDR es una notación utilizada para representar bloques de direcciones IP de manera eficiente, lo que
permite una asignación más flexible y eficiente de direcciones IP en redes de computadoras.

Este Script esta creado precisamente con esa finalidad simplemente debes de ingresar tu ip seguido de la cantidad
de bits para la mascara de red que deseas ver seria algo asi por ejemplo: 111.111.11.1/24