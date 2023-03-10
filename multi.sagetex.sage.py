## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file multi.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_130 = Integer(130); _sage_const_132 = Integer(132); _sage_const_137 = Integer(137); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_138 = Integer(138); _sage_const_139 = Integer(139); _sage_const_140 = Integer(140); _sage_const_141 = Integer(141); _sage_const_142 = Integer(142); _sage_const_5 = Integer(5); _sage_const_172 = Integer(172); _sage_const_6 = Integer(6); _sage_const_25 = Integer(25); _sage_const_16 = Integer(16); _sage_const_193 = Integer(193); _sage_const_7 = Integer(7); _sage_const_9 = Integer(9); _sage_const_210 = Integer(210); _sage_const_8 = Integer(8); _sage_const_278 = Integer(278); _sage_const_286 = Integer(286); _sage_const_10 = Integer(10); _sage_const_306 = Integer(306); _sage_const_11 = Integer(11); _sage_const_325 = Integer(325); _sage_const_12 = Integer(12); _sage_const_327 = Integer(327); _sage_const_13 = Integer(13); _sage_const_333 = Integer(333); _sage_const_14 = Integer(14); _sage_const_339 = Integer(339); _sage_const_15 = Integer(15); _sage_const_348 = Integer(348); _sage_const_418 = Integer(418); _sage_const_17 = Integer(17); _sage_const_435 = Integer(435); _sage_const_18 = Integer(18); _sage_const_446 = Integer(446); _sage_const_19 = Integer(19); _sage_const_451 = Integer(451); _sage_const_20 = Integer(20); _sage_const_464 = Integer(464); _sage_const_21 = Integer(21); _sage_const_521 = Integer(521); _sage_const_22 = Integer(22); _sage_const_545 = Integer(545); _sage_const_23 = Integer(23); _sage_const_551 = Integer(551); _sage_const_24 = Integer(24); _sage_const_552 = Integer(552); _sage_const_583 = Integer(583); _sage_const_586 = Integer(586); _sage_const_593 = Integer(593); _sage_const_26 = Integer(26); _sage_const_638 = Integer(638); _sage_const_27 = Integer(27); _sage_const_660 = Integer(660); _sage_const_28 = Integer(28); _sage_const_675 = Integer(675); _sage_const_29 = Integer(29); _sage_const_750 = Integer(750); _sage_const_30 = Integer(30); _sage_const_807 = Integer(807); _sage_const_31 = Integer(31); _sage_const_839 = Integer(839); _sage_const_32 = Integer(32); _sage_const_876 = Integer(876); _sage_const_33 = Integer(33); _sage_const_908 = Integer(908); _sage_const_34 = Integer(34); _sage_const_942 = Integer(942); _sage_const_35 = Integer(35); _sage_const_1115 = Integer(1115); _sage_const_1117 = Integer(1117); _sage_const_1118 = Integer(1118); _sage_const_36 = Integer(36); _sage_const_0p5 = RealNumber('0.5'); _sage_const_1133 = Integer(1133); _sage_const_37 = Integer(37); _sage_const_1148 = Integer(1148); _sage_const_38 = Integer(38); _sage_const_1168 = Integer(1168); _sage_const_39 = Integer(39); _sage_const_1190 = Integer(1190); _sage_const_40 = Integer(40); _sage_const_1215 = Integer(1215); _sage_const_41 = Integer(41); _sage_const_1295 = Integer(1295); _sage_const_42 = Integer(42)## This file (multi.sagetex.sage) was *autogenerated* from multi.tex with sagetex.sty version 2021/10/16 v3.6.
import sagetex
_st_ = sagetex.SageTeXProcessor('multi', version='2021/10/16 v3.6', version_check=True)
_st_.current_tex_line = _sage_const_130 
_st_.blockbegin()
try:
 var('x y z')
except:
 _st_.goboom(_sage_const_132 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_137 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2 /_sage_const_2 +y**_sage_const_2 /_sage_const_3  + z**_sage_const_2 /_sage_const_4  == _sage_const_1  , (x,-_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, -_sage_const_2 , _sage_const_2 )),frame=False)
except:
 _st_.goboom(_sage_const_137 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2 /_sage_const_2 +y**_sage_const_2 /_sage_const_3  == z**_sage_const_2 /_sage_const_4  , (x,-_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, -_sage_const_2 , _sage_const_2 ),frame=False))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_139 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2 /_sage_const_2 +y**_sage_const_2 /_sage_const_3  == z/_sage_const_4  , (x,-_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, -_sage_const_2 , _sage_const_2 ),frame=False))
except:
 _st_.goboom(_sage_const_139 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2 /_sage_const_2 +y**_sage_const_2 /_sage_const_3  - z**_sage_const_2 /_sage_const_4 ==_sage_const_1  , (x,-_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, -_sage_const_2 , _sage_const_2 ),frame=False))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2 /_sage_const_2 +y**_sage_const_2 /_sage_const_3  == z/_sage_const_4  , (x,-_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, -_sage_const_2 , _sage_const_2 ),frame=False))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=implicit_plot3d(-x**_sage_const_2 /_sage_const_2 -y**_sage_const_2 /_sage_const_3  + z**_sage_const_2 /_sage_const_4 ==_sage_const_1  , (x,-_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, -_sage_const_2 , _sage_const_2 ),frame=False))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_172 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=implicit_plot3d(z == _sage_const_25  - x**_sage_const_2  - y**_sage_const_2 , (x, -_sage_const_3 , _sage_const_3 ), (y, -_sage_const_3 , _sage_const_3 ), (z, _sage_const_16 , _sage_const_25 )))
except:
 _st_.goboom(_sage_const_172 )
try:
 _st_.current_tex_line = _sage_const_193 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=plot(sqrt(_sage_const_9 -x**_sage_const_2 ), (x, -_sage_const_3 , _sage_const_3 )) + plot(_sage_const_0 , (x, -_sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_193 )
try:
 _st_.current_tex_line = _sage_const_210 
 _st_.plot(_sage_const_8 , format='notprovided', _p_=plot(-sqrt(_sage_const_1 -x**_sage_const_2 ), (x, -_sage_const_1 , _sage_const_1 )))
except:
 _st_.goboom(_sage_const_210 )
try:
 _st_.current_tex_line = _sage_const_278 
 _st_.plot(_sage_const_9 , format='notprovided', _p_=polygon([[_sage_const_0 ,_sage_const_0 ], [_sage_const_0 , _sage_const_2 ], [_sage_const_1 ,_sage_const_2 ]], color='red'))
except:
 _st_.goboom(_sage_const_278 )
try:
 _st_.current_tex_line = _sage_const_286 
 _st_.plot(_sage_const_10 , format='notprovided', _p_=polygon([[_sage_const_0 ,_sage_const_0 ], [_sage_const_0 , _sage_const_2 ], [_sage_const_1 ,_sage_const_2 ]], color='red') + plot(sqrt(_sage_const_4 -x**_sage_const_2 ), (x, _sage_const_0 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_286 )
try:
 _st_.current_tex_line = _sage_const_306 
 _st_.plot(_sage_const_11 , format='notprovided', _p_=region_plot(y<=sqrt(_sage_const_5 -x**_sage_const_2 ), (x, _sage_const_0 , _sage_const_1 ), (y, _sage_const_1 ,_sage_const_3 )))
except:
 _st_.goboom(_sage_const_306 )
try:
 _st_.current_tex_line = _sage_const_325 
 _st_.plot(_sage_const_12 , format='notprovided', _p_=implicit_plot3d(z==_sage_const_5 -x**_sage_const_2 -y**_sage_const_2 , (x,-_sage_const_2 ,_sage_const_2  ), (y, -_sage_const_2 ,_sage_const_2 ), (z, _sage_const_1 , _sage_const_5 ), region=(lambda x,y,z: z >=_sage_const_1 )))
except:
 _st_.goboom(_sage_const_325 )
try:
 _st_.current_tex_line = _sage_const_327 
 _st_.plot(_sage_const_13 , format='notprovided', _p_=implicit_plot(x**_sage_const_2 +y**_sage_const_2 ==_sage_const_4 , (x, -_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_327 )
try:
 _st_.current_tex_line = _sage_const_333 
 _st_.plot(_sage_const_14 , format='notprovided', _p_=region_plot(y<=_sage_const_4 -x, (x, -_sage_const_1 , _sage_const_0 ), (y, _sage_const_1 , _sage_const_5 )))
except:
 _st_.goboom(_sage_const_333 )
try:
 _st_.current_tex_line = _sage_const_339 
 _st_.plot(_sage_const_15 , format='notprovided', _p_=region_plot(y<=_sage_const_4 , (x, -_sage_const_1 , _sage_const_2 ), (y, -_sage_const_3 , _sage_const_4 )))
except:
 _st_.goboom(_sage_const_339 )
try:
 _st_.current_tex_line = _sage_const_348 
 _st_.plot(_sage_const_16 , format='notprovided', _p_=region_plot(y<=_sage_const_2 , (x, -_sage_const_1 , _sage_const_0 ), (y, _sage_const_0 , _sage_const_2 )) + region_plot(y<=sqrt(_sage_const_4 -x**_sage_const_2 ), (x, _sage_const_0 , _sage_const_2 ), (y, _sage_const_0 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_348 )
try:
 _st_.current_tex_line = _sage_const_418 
 _st_.plot(_sage_const_17 , format='notprovided', _p_=implicit_plot3d(z**_sage_const_2  == x**_sage_const_2 +y**_sage_const_2 , (x, -_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, _sage_const_0 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_418 )
try:
 _st_.current_tex_line = _sage_const_435 
 _st_.plot(_sage_const_18 , format='notprovided', _p_= plot3d(x**_sage_const_2 +y**_sage_const_2 , (x,-_sage_const_1 , _sage_const_1 ), (y, -_sage_const_1 , _sage_const_1 )) + implicit_plot3d(x**_sage_const_2  + y**_sage_const_2  ==_sage_const_1 , (x, -_sage_const_1 ,_sage_const_1 ), (y, -_sage_const_1 ,_sage_const_1 ), (z, _sage_const_1 , _sage_const_2 )) + plot3d(_sage_const_2 , (x, -_sage_const_1 ,_sage_const_1 ), (y, -_sage_const_1 , _sage_const_1 )))
except:
 _st_.goboom(_sage_const_435 )
try:
 _st_.current_tex_line = _sage_const_446 
 _st_.plot(_sage_const_19 , format='notprovided', _p_=region_plot(y >= x**_sage_const_2 , (x, -_sage_const_1 , _sage_const_1 ), (y, _sage_const_0 , _sage_const_1 )) + region_plot(y<=_sage_const_2 , (x, -_sage_const_1 , _sage_const_1 ), (y, _sage_const_1 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_446 )
try:
 _st_.current_tex_line = _sage_const_451 
 _st_.plot(_sage_const_20 , format='notprovided', _p_=plot3d(_sage_const_1 -sqrt(x**_sage_const_2 +y**_sage_const_2 ), (x, -_sage_const_1 , _sage_const_1 ), (y, -_sage_const_1 , _sage_const_1 )) + plot3d(-_sage_const_1 +x**_sage_const_2 +y**_sage_const_2 , (x, -_sage_const_1 , _sage_const_1 ), (y, -_sage_const_1 , _sage_const_1 )))
except:
 _st_.goboom(_sage_const_451 )
try:
 _st_.current_tex_line = _sage_const_464 
 _st_.plot(_sage_const_21 , format='notprovided', _p_=region_plot([y<sqrt(_sage_const_9 -x**_sage_const_2 ), y > _sage_const_1 ], (x, _sage_const_1 , _sage_const_2 ), (y, _sage_const_1 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_464 )
try:
 _st_.current_tex_line = _sage_const_521 
 _st_.plot(_sage_const_22 , format='notprovided', _p_=parametric_plot((_sage_const_2 *cos(x), _sage_const_2 *sin(x)), (x, _sage_const_0 , pi)))
except:
 _st_.goboom(_sage_const_521 )
try:
 _st_.current_tex_line = _sage_const_545 
 _st_.plot(_sage_const_23 , format='notprovided', _p_=plot_vector_field((x + y, _sage_const_2 *x - y), (x, -_sage_const_3 , _sage_const_3 ), (y, -_sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_545 )
try:
 _st_.current_tex_line = _sage_const_551 
 _st_.plot(_sage_const_24 , format='notprovided', _p_=plot_vector_field((x,y), (x, -_sage_const_3 , _sage_const_3 ), (y, -_sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_551 )
try:
 _st_.current_tex_line = _sage_const_552 
 _st_.plot(_sage_const_25 , format='notprovided', _p_=plot_vector_field((-y, x), (x, -_sage_const_3 , _sage_const_3 ), (y, -_sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_552 )
_st_.current_tex_line = _sage_const_583 
_st_.blockbegin()
try:
 # I am going to do this later
 print('hello world')
except:
 _st_.goboom(_sage_const_586 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_593 
 _st_.plot(_sage_const_26 , format='notprovided', _p_=plot_vector_field((_sage_const_2 *y, _sage_const_1 ), (x, -_sage_const_3 , _sage_const_3 ), (y, -_sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_593 )
try:
 _st_.current_tex_line = _sage_const_638 
 _st_.plot(_sage_const_27 , format='notprovided', _p_=plot_vector_field((_sage_const_2 , _sage_const_4 *y), (x, _sage_const_0 , _sage_const_10 ), (y, _sage_const_0 , _sage_const_10 )) + streamline_plot((_sage_const_2 , _sage_const_4 *y), (x, _sage_const_0 , _sage_const_10 ), (y, _sage_const_0 , _sage_const_10 ), start_points=[[_sage_const_3 ,_sage_const_5 ]]))
except:
 _st_.goboom(_sage_const_638 )
try:
 _st_.current_tex_line = _sage_const_660 
 _st_.plot(_sage_const_28 , format='notprovided', _p_=plot(_sage_const_2 *x+_sage_const_2 , (x, -_sage_const_1 , _sage_const_0 )) + plot(sqrt(_sage_const_4 -x**_sage_const_2 ), (x, _sage_const_0 , _sage_const_2 )) + plot_vector_field((x+y, x), (x, -_sage_const_1 , _sage_const_2 ), (y, _sage_const_0 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_660 )
try:
 _st_.current_tex_line = _sage_const_675 
 _st_.plot(_sage_const_29 , format='notprovided', _p_=plot(x**_sage_const_2 , (x, -_sage_const_1 , _sage_const_2 )) + plot_vector_field((_sage_const_2 , x), (x, -_sage_const_1 , _sage_const_2 ), (y, _sage_const_0 , _sage_const_4 )))
except:
 _st_.goboom(_sage_const_675 )
try:
 _st_.current_tex_line = _sage_const_750 
 _st_.plot(_sage_const_30 , format='notprovided', _p_=parametric_plot((x, _sage_const_0 ), (x, -_sage_const_1 , _sage_const_0 ), thickness=_sage_const_5 ) + parametric_plot((_sage_const_0 , x), (x, _sage_const_0 , _sage_const_1 ), thickness=_sage_const_5 ) + plot_vector_field((y**_sage_const_2 , _sage_const_2 *x*y+_sage_const_1 ), (x, -_sage_const_1 , _sage_const_0 ), (y, _sage_const_0 , _sage_const_1 )))
except:
 _st_.goboom(_sage_const_750 )
try:
 _st_.current_tex_line = _sage_const_807 
 _st_.plot(_sage_const_31 , format='notprovided', _p_=plot_vector_field((_sage_const_2 *x*y + y**_sage_const_2 , x**_sage_const_2 *y + x), (x, -_sage_const_5 , _sage_const_5 ), (y, -_sage_const_5 , _sage_const_5 )))
except:
 _st_.goboom(_sage_const_807 )
try:
 _st_.current_tex_line = _sage_const_839 
 _st_.plot(_sage_const_32 , format='notprovided', _p_=plot_vector_field((-y/sqrt(x**_sage_const_2 +y**_sage_const_2 ), x/sqrt(x**_sage_const_2 +y**_sage_const_2 )), (x, -_sage_const_3 , _sage_const_3 ), (y, -_sage_const_3 , _sage_const_3 )) + parametric_plot((_sage_const_2 *sin(x), _sage_const_2 *cos(x)), (x, _sage_const_0 , _sage_const_2 *pi)))
except:
 _st_.goboom(_sage_const_839 )
try:
 _st_.current_tex_line = _sage_const_876 
 _st_.plot(_sage_const_33 , format='notprovided', _p_=plot_vector_field((_sage_const_2 *y, -_sage_const_2 *x), (x, -_sage_const_3 , _sage_const_3 ), (y, -_sage_const_3 , _sage_const_3 )) + parametric_plot((_sage_const_0 , x), (x, -_sage_const_3 , _sage_const_3 )) + parametric_plot((_sage_const_3 *cos(x),_sage_const_3 *sin(x)), (x, -pi/_sage_const_2 , pi/_sage_const_2 )))
except:
 _st_.goboom(_sage_const_876 )
try:
 _st_.current_tex_line = _sage_const_908 
 _st_.plot(_sage_const_34 , format='notprovided', _p_=plot_vector_field((x*y+_sage_const_1 , x), (x, _sage_const_0 , _sage_const_2 ), (y, _sage_const_0 , _sage_const_3 )) + parametric_plot((x, _sage_const_3 -_sage_const_3 /_sage_const_2 *x), (x, _sage_const_0 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_908 )
try:
 _st_.current_tex_line = _sage_const_942 
 _st_.plot(_sage_const_35 , format='notprovided', _p_=region_plot(y <= sin(x), (x, _sage_const_0 , pi), (y, _sage_const_0 , _sage_const_1 )))
except:
 _st_.goboom(_sage_const_942 )
_st_.current_tex_line = _sage_const_1115 
_st_.blockbegin()
try:
     from sage.plot.plot3d.shapes import Cylinder
     
except:
 _st_.goboom(_sage_const_1117 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_1118 
 _st_.plot(_sage_const_36 , format='notprovided', _p_=Cylinder(_sage_const_1 , _sage_const_1 , closed=False) + arrow((_sage_const_0 , _sage_const_1 , _sage_const_0p5 ), (_sage_const_0 , _sage_const_2 , _sage_const_0p5 )))
except:
 _st_.goboom(_sage_const_1118 )
try:
 _st_.current_tex_line = _sage_const_1133 
 _st_.plot(_sage_const_37 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2  + z**_sage_const_2  == _sage_const_4 **_sage_const_2 , (x, -_sage_const_4 , _sage_const_4 ), (y, -_sage_const_2 , _sage_const_3 ), (z, -_sage_const_4 , _sage_const_4 )) + plot_vector_field3d((y, x+_sage_const_1 , z), (x, -_sage_const_4 , _sage_const_4 ), (y, -_sage_const_2 , _sage_const_3 ), (z, -_sage_const_4 , _sage_const_4 )))
except:
 _st_.goboom(_sage_const_1133 )
try:
 _st_.current_tex_line = _sage_const_1148 
 _st_.plot(_sage_const_38 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2  + z**_sage_const_2  + y**_sage_const_2  == _sage_const_2 **_sage_const_2 , (x, -_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, _sage_const_0 , _sage_const_2 )) + plot_vector_field3d((_sage_const_1 , z, y), (x, -_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, _sage_const_0 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_1148 )
try:
 _st_.current_tex_line = _sage_const_1168 
 _st_.plot(_sage_const_39 , format='notprovided', _p_=implicit_plot3d(y==sqrt(x**_sage_const_2 +z**_sage_const_2 ), (x, -_sage_const_3 , _sage_const_3 ), (y, _sage_const_0 , _sage_const_2 ), (z, -_sage_const_3 , _sage_const_3 ) ) + plot_vector_field3d((_sage_const_1 +z, x, y), (x, -_sage_const_3 , _sage_const_3 ), (y, _sage_const_0 , _sage_const_3 ), (z, -_sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_1168 )
try:
 _st_.current_tex_line = _sage_const_1190 
 _st_.plot(_sage_const_40 , format='notprovided', _p_=implicit_plot3d(x**_sage_const_2  + z**_sage_const_2  + y**_sage_const_2  == _sage_const_2 **_sage_const_2 , (x, -_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, _sage_const_0 , _sage_const_2 )) + plot_vector_field3d((x, y, z), (x, -_sage_const_2 , _sage_const_2 ), (y, -_sage_const_2 , _sage_const_2 ), (z, _sage_const_0 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_1190 )
try:
 _st_.current_tex_line = _sage_const_1215 
 _st_.plot(_sage_const_41 , format='notprovided', _p_=implicit_plot3d(y == _sage_const_2 -x**_sage_const_2 -z**_sage_const_2 , (x, -_sage_const_3 , _sage_const_3 ), (y, _sage_const_0 , _sage_const_2 ), (z, -_sage_const_3 , _sage_const_3 )) + plot_vector_field3d((y, _sage_const_2 *x+_sage_const_1 , y+z), (x,-_sage_const_3 , _sage_const_3 ), (y, _sage_const_0 , _sage_const_2 ), (z, -_sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_1215 )
try:
 _st_.current_tex_line = _sage_const_1295 
 _st_.plot(_sage_const_42 , format='notprovided', _p_=list_plot3d([(_sage_const_2 ,_sage_const_0 ,_sage_const_0 ), (_sage_const_0 ,_sage_const_2 ,_sage_const_0 ), (_sage_const_0 ,_sage_const_0 ,_sage_const_2 )]) + plot_vector_field3d((_sage_const_3 *x, _sage_const_3 *y, _sage_const_3 *z), (x,-_sage_const_2 , _sage_const_2 ), (y, _sage_const_0 , _sage_const_2 ), (z, _sage_const_0 , _sage_const_2 )))
except:
 _st_.goboom(_sage_const_1295 )
_st_.endofdoc()

