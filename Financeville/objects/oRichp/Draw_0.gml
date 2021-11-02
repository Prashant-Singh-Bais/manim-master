/// @description health bar
// You can write your code in this editor
draw_self();

var x1 = x - (sprite_width/2);
var x2 = x + (sprite_width/2);
var y1 = (y - (sprite_height/2))-8;
var y2 = (y - (sprite_height/2))-16;

var amount = (hp_current/hp_max)*100;

draw_healthbar(x1, y1, x2, y2, amount, c_black, c_red, c_green, 0, true, true);

