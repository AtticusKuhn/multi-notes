## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file multi.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_130 = Integer(130); _sage_const_132 = Integer(132); _sage_const_137 = Integer(137); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_138 = Integer(138); _sage_const_139 = Integer(139); _sage_const_140 = Integer(140); _sage_const_141 = Integer(141); _sage_const_142 = Integer(142); _sage_const_5 = Integer(5); _sage_const_172 = Integer(172); _sage_const_6 = Integer(6); _sage_const_25 = Integer(25); _sage_const_16 = Integer(16); _sage_const_193 = Integer(193); _sage_const_7 = Integer(7); _sage_const_9 = Integer(9); _sage_const_210 = Integer(210); _sage_const_8 = Integer(8); _sage_const_278 = Integer(278); _sage_const_286 = Integer(286); _sage_const_10 = Integer(10); _sage_const_306 = Integer(306); _sage_const_11 = Integer(11); _sage_const_325 = Integer(325); _sage_const_12 = Integer(12); _sage_const_327 = Integer(327); _sage_const_13 = Integer(13); _sage_const_333 = Integer(333); _sage_const_14 = Integer(14); _sage_const_339 = Integer(339); _sage_const_15 = Integer(15); _sage_const_348 = Integer(348)## This file (multi.sagetex.sage) was *autogenerated* from multi.tex with sagetex.sty version 2021/10/16 v3.6.
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
_st_.endofdoc()

