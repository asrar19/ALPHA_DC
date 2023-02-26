function check(){
var c=0;
var q1=document.building_dc.question1.value;
var q2=document.building_dc.question2.value;
var q3=document.building_dc.question3.value;

if(q1=="0-30"){c++}
if(q2=="1"){c++}
if(q3=="small"){c++}

    document.write(c);


}