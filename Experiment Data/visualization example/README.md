by Lingkun Kong 5140219016

the generating sequence order is:

original_pic
->
conv1_vect (or extract_vect) (vect means vectors)
->
conv1_feat (feat means feature)
->
conv2_feat
->
...
->
conv9_feat
->
deconv (or final_deconv)
->
final_resized
->
fusing_together
->
final