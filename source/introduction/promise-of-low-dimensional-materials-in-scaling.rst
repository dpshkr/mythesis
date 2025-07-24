Promise of low-dimensional materials in transistor scaling
============================================================

Transistors are fundamental building blocks of all modern computational systems.
Therefore, the efficiency of a transistor, in terms of energy and speed, will have a major impact on the overall system's performance.
The number of transistors in a computational system has grown remarkably since the 1960s, guided by Moore's law :cite:p:`moore1998cramming`.
The transistor dimensions have consistently reduced, making it possible to pack more transistors into a single chip with the same area :cite:p:`dennard1974design`.
Interestingly, this has consistently led computation systems to perform better for lower costs over the past half-century.
In a very short time, this exponential growth greatly impacted human society's social, economic, and cultural aspects.
Silicon, a three-dimensional material, has been the material for transistor channels.
However, as the silicon transistors enter the sub-10nm technology node, the technological challenges are also ever-increasing.
To overcome these challenges, novel device architectures and materials to make transistors are being continuously explored by the global research community.

Transistors are switches in which the current between two terminals (source and drain) is controlled by a third terminal (gate).
The electrostatics of the transistor channel mainly governs the transistor's properties. 
The electrostatic potential along the channel of the transistor is given by :cite:p:`suzuki1993scaling`

.. math::

    \frac{d^2\phi (x)}{dx^2} - \frac{\phi(x)}{\lambda^2} = 0


where :math:`\phi (x)` is the electrostatic potential along the channel of the device, while :math:`\lambda=\sqrt{\frac{t_bt_{ox}\epsilon_b}{\epsilon_{ox}}}` 
is called the characteristic length of the transistor.
A smaller characteristic length allows for a smaller transistor without affecting the performance.
Here :math:`t_b`, :math:`\epsilon_b`, :math:`t_{ox}`, and :math:`\epsilon_{ox}` are the thickness and dielectric constants of the semiconducting channel and the gate dielectric, respectively.
A significant effort has been put into improving the gate stack by reducing :math:`t_{ox}` and increasing :math:`\epsilon_{ox}`.
At the same time, efforts to reduce the thickness of the transistor channel, :math:`t_b`, have also been significant.
However, the effort to reduce :math:`t_b` has always been met with challenges like increased surface roughness, device variability, and poor interfaces due to dangling bonds.
These effects are most significantly visible in the degradation of field-effect mobility of the transistors with decreasing :math:`t_b` due to an increase in carrier scattering.

Here is where low-dimensional materials have come to the rescue.
Due to their weak van der Waals bonding along some dimensions, they can be arbitrarily thinned down along those dimensions without significantly degrading the channel and interface properties :cite:`liu2021promises`.
A two-dimensional material can be scaled down to a monolayer without degrading its properties :cite:p:`novoselov2005two,radisavljevic2011single`. 
Similarly, a one-dimensional material can be scaled to a single chain of atoms/molecules.

However, low-dimensional semiconductors come with a different set of challenges, which the research community is trying to address.
Foremost among these is the lack of proper contact with the material.
Inefficient metal-semiconductor contacts lead to large contact resistance, significantly degrading the transistor performance :cite:p:`ngo2020control`.
Also, the lack of proper doping techniques and the dependence on intrinsic doping of the material often leads to significant device-to-device variations. 
The lack of doping has also made implementing complementary logic (*n*-type and *p*-type) challenging. 
Finally, the wafer-scale fabrication of integrated circuits also remains a challenge.
