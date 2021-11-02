/// @description Insert description here
// You can write your code in this editor



 
key_right =keyboard_check(ord("D"))
key_left = keyboard_check(ord("A"))
key_jump = (keyboard_check_pressed(vk_space));



var move = key_right - key_left;

hsp = move * walksp;
vsp = grv;

//jump
if (place_meeting(x,y+1,oWall)) 
{
	if (place_meeting(x+1,y,oWall)) 
	{
		vsp = -32;
		if (place_meeting(x+1,y,oWall)) and (vsp>0) 
		{vsp =0;}
		
		
	}
	if (place_meeting(x-1,y,oWall)) 
	{
		vsp = -32;
		if (place_meeting(x+1,y,oWall)) and (vsp<0)
		{vsp =0;}
	
	}
}
// horizontal collision
if (place_meeting(x+hsp,y,oWall)) and (vsp>0)
{
	while (!place_meeting(x+sign(hsp),y,oWall))
	{
		x = x + sign(hsp);
	}
	hsp = 0;
}

// vertical collision
if (place_meeting(x,y+vsp,oWall)) and (vsp>0)
{
	while (!place_meeting(x,y+sign(vsp),oWall))
	{
		y = y + sign(vsp);
	}
	vsp = 0;
}


x = x + hsp; 
y = y + vsp;


// health bar

if (place_meeting(x,y,oIbox))
{
	//osc1
	if mytextbox == noone
		{mytextbox = instance_create_layer(x-1,y+200,"Textl",osc1)}
	if (!place_meeting(x,y,oIbox)) 
	{
		instance_destroy(mytextbox)
	}

	//osc2
	
	
	if (keyboard_check(vk_enter))
		{
			instance_destroy(mytextbox)
		
			if mytextbox2 == noone
			{	
				mytextbox2 = instance_create_layer(x-1,y+200,"Textl",osc2);
			}
		}

// carona
	if (keyboard_check(ord("2"))) 
		{
				//hp_current -= 40;
			choice = 2;
			instance_destroy(mytextbox2)
			if richcarona == noone
			{
				richcarona = instance_create_layer(x-10,y-5,"Textl",ocarona);
				i = instance_create_layer(x+30,y-30,"Textl",ocaronatext);
				}
		}
			
	if (keyboard_check(vk_enter)) and (richcarona!=noone)
				{
				 j = instance_create_layer(x,y,"Textl",ocaronap);
				
				}
	//timer -= 1;
	//if timer == 0  and (j!=noone)
	if keyboard_check(vk_enter) and (j!=noone)
	
				 {
					 instance_destroy(ocaronap)
					 instance_destroy(i)
					 instance_destroy(richcarona)
					 k = instance_create_layer(x+20,y-5,"Textl",fullyr);
					 hp_current -= 10;
					 timer = room_speed*5;
				 }
	timer -= 1;
	if timer == 0  and (k!=noone)
				 {
					 instance_destroy(k)
					 timer = room_speed*5;
				 }
	if (!place_meeting(x,y,oIbox)) 
		{	
					instance_destroy(mytextbox2);
		}		

//upgrade

	
if (keyboard_check(ord("3"))) 
		{
				//hp_current -= 40;
			choice = 3;
			instance_destroy(mytextbox2)
			if richupgrade == noone
			{
				richupgrade = instance_create_layer(x+1,y+200,"Textl",up_choices);
				//i = instance_create_layer(x+30,y-30,"Textl",ocaronatext);
				}
		}
		//wedding
		
	
		
	if (keyboard_check(ord("1")))  and (choice = 3)
				{
				instance_destroy(richupgrade);
				rin = instance_create_layer(x+5,y-5,"Textl",ring);
				
				}
	 
	if (rin != noone) and (keyboard_check(vk_enter))
			{
					 ctxt = instance_create_layer(x+1,y+200,"Textl",textconvert)
					 //pass += 1;
					 //hp_current -= 10;
					 //timer = room_speed*5;
					 //timer -= 1;
				 }
	
	if  (ctxt != noone) and (keyboard_check(vk_enter))
				 {
					stx = instance_create_layer(x+5,y-5,"Textl",Ostock) ;
					instance_destroy(ctxt);
					//pass += 1;
					 //timer = room_speed*5;
					  //timer -= 1;
				 }

	if (stx != noone) and (keyboard_check(vk_enter))
				 {
					 married = instance_create_layer(x-1,y+200,"Textl",marriagedone) 
					
					
					 //timer = room_speed*5;
				 }
	if (married != noone) and (keyboard_check(vk_enter))
		{
			instance_destroy(rin);
			instance_destroy(stx);
					
		}

	if (!place_meeting(x,y,oIbox)) 
		{	
					instance_destroy(mytextbox2);
		}		
}

