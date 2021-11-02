/// @description Insert description here
// You can write your code in this editor


 
key_right =(keyboard_check(vk_right));
key_left = (keyboard_check(vk_left));
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
	if mytextbox == noone
		{mytextbox = instance_create_layer(x-1,y+200,"Textl",osc1)}
	if (!place_meeting(x,y,oIbox))
{
	instance_destroy(mytextbox)
}
	if keyboard_check(ord("1"))
		{
			hp_current -= 20;
			instance_destroy(otextbox);
		}
		if keyboard_check(ord("2"))
		{
			hp_current -= 40;
			instance_destroy(otextbox);
		}
		if keyboard_check(ord("3"))
		{
			hp_current -= 30;
			instance_destroy(otextbox);
		}
}
	
