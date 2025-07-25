Contact-Barrier Free, High Mobility, Dual-Gated Junctionless Transistor Using Tellurium Nanowire
===================================================================================================

The tight electrostatic control in multi-gated nanowire field effect transistor (FET) :cite:p:`cui2003high,singh2006high,appenzeller2008toward,kuhn2012considerations` makes it one of the most promising candidates for further scaling of silicon technology in sub-5 nm technology nodes, and is being actively pursued by the semiconductor industry :cite:p:`bohr2017cmos,Samsung_Plans_Mass`. The possible vertical integration of multiple nanowires enhances the drive current at a given footprint :cite:p:`lee2016vertically,Samsung_Plans_Mass`.
In parallel, several high-mobility, non-silicon channel options are being actively pursued as well, particularly for the p-FET :cite:p:`ikeda2012high,fang2007vertically,wang2003germanium`.

Three technological roadblocks must be overcome to achieve these high-performance, ultra-scaled devices. First, the source-drain electrical isolation in a transistor is usually achieved by doping. The required spatial steepness of the doping profile is non-trivial to achieve in such ultra-short channel nanowire FETs. It also adds to the large variability, resulting in low yield. In this direction, junctionless FET has attracted a lot of attention for high scalability :cite:p:`lee2009junctionless,gundapaneni2011enhanced` where one uses a narrow conducting channel, and the gate voltage is used to deplete the carriers from the channel to turn it off, thus avoiding source-drain junction formation through ion implantation. Second, since the nanowire must be very narrow to achieve the required gate control, the surface roughness scattering is enhanced :cite:p:`jin2007modeling,ramayya2008electron`, significantly degrading the carrier mobility. A nanowire channel with a dangling-bond-free surface will be ideally suited to reduce such mobility degradation. Third, as the device footprint goes down with transistor scaling, the effective contact area at the source and drain reduces. This increases the fraction of the contact resistance in the total transistor resistance under on condition, which is detrimental to the overall drive current, switching speed, current saturation, and output resistance :cite:p:`majumdar2010effects`. One must use novel techniques to reduce contact resistivity.

In an attempt to address the above-mentioned issues, this chapter presents a dual-gated tellurium (Te) nanowire junctionless transistor. The unique chiral nature of the nanowire crystal structure :cite:p:`liang2009synthesis,qin2020raman` allows a high hole mobility due to a dangling-bond-free surface, and its low electron affinity helps us to achieve zero Schottky barrier at the contact interface, reducing the contact resistance. We achieve a drive current of 216 µA/µm with an on-off ratio of 2×10⁴ and a high hole mobility of 570 cm²/V·s.

Te is an element in the chalcogen group, and its crystal structure consists of covalently bonded one-dimensional chains of Te along the c-axis that are held together by weak van der Waals interactions [inset of :ref:`Figure 2.1 <ch01-material-char-01>`\(a)]. Thus, the nanowire form of Te is predominantly bound by lower energy surfaces that are produced by only breaking the weak van der Waals bonds and not the strong covalent bonds, leading to the dangling-bond-free surface of the nanowire. This unique anisotropic crystal structure of Te provides an opportunity to synthesize nanowires of Te down to single chain Te atoms :cite:p:`medeiros2017single,qin2020raman`.


Tellurium, in its bulk form, has a bandgap of 0.35 eV and exhibits *p*-type nature :cite:p:`zhao2020evaporated` with high carrier
mobility :cite:`zhu2017multivalency`. As the bulk Te is reduced to smaller dimensions, it starts exhibiting an indirect bandgap of about 0.6 eV :cite:p:`roy2017manipulation,qin2020raman`. In addition to these electrical properties, Te also shows remarkable optical, thermoelectric, and piezoelectric properties :cite:p:`lee2013high,pradhan2017ultra,qiu2019thermoelectric,lin2016tellurium`.

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   synthesis-and-characterization-of-te-nanowires
   device-fabrication
