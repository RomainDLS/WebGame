var pong = {
	ball : function() {
		var z = document.outerWidth || document.documentElement.clientWidth || document.body.clientWidth,
		zz = document.innerHeight || document.documentElement.clientHeight || document.body.clientWidth,
		content,
		x = 65, /* Starting Xposition */
		y = 110, /* Starting Yposition */
		WIDTH = z * (3/4),
		HEIGHT = zz * (3/4),
		dx = 8,
		dy = 0,
		pox = 50,
		poy = 50,
		ptx = WIDTH - 50,
		pty = 50,
		doy = 20,
		dty = 20,
		flag = 0,
		impact,
		scores = {Joueur1Score : 0, Joueur2Score : 0},
		keys = [],
		a,
		c = 0;
		var canvas = document.getElementById('canvas');
		canvas.setAttribute('width',WIDTH);
		canvas.setAttribute('height',HEIGHT);
	
		function init() {
		content = canvas.getContext("2d");
		return setInterval(draw, 15);
		}
		
		function rect(x,y,w,h) {
		content.beginPath();
		content.rect(x,y,w,h);
		content.closePath();
		content.fill();
		content.strokeStyle = '#fff';
		content.lineWidth = '5px';
		content.beginPath();
		content.moveTo(w/2,0);
		content.lineTo(w/2,h);
		content.stroke();
		content.closePath();
		} 
		function circle(x,y,r) {
		content.beginPath();
		content.arc(x, y, r, 0, Math.PI*2, true);
		content.fill();
		}
		function j1Rect(pox,poy,pow,poh) {
		content.beginPath();
		content.rect(pox,poy,pow,poh);
		content.closePath();
		content.fill();
		}
		function j1Score(ox,oy) {
		content.font = '60px sans-serif';
		content.strokeText(scores.Joueur1Score,ox,oy);
		}
		function j2Rect(ptx,pty,pow,poh) {
		content.beginPath();
		content.rect(ptx,pty,pow,poh);
		content.closePath();
		content.fill();
		}
		function j2Score(tx,ty) {
		content.font = '60px sans-serif';
		content.strokeText(scores.Joueur2Score,tx,ty);
		}
		function clear() {
		content.clearRect(0, 0, WIDTH, HEIGHT);
		}
		onKeyDown = onKeyUp = function(event) {
			event.preventDefault();
			keys[event.keyCode] = event.type == 'keydown';
			if(keys[32]) {
				if(flag == 0) {
					flag = 1;
				}
			}
			if(keys[65]) {
				if(poy - doy > -15) {
					if(flag == 0 && x == 65) {
						poy -= doy;
						y -= doy;
					}
					else { 
						poy -= doy;
					}		
				}
			}
			if(keys[81]) {
				if(poy + doy < HEIGHT - 105) {
					if(flag == 0 && x == 65) {
						poy += doy;
						y += doy;
					}
					else {
						poy += doy;
					}
				}
			}
			if(keys[38]) {
				if(pty - dty > -15) {
					if(flag == 0 && x == WIDTH - 61) {
						pty -= dty;
						y -= dty;
					}
					else {
						pty -= dty;
					}	
				}
			}
			if(keys[40]) {
				if(pty + dty < HEIGHT - 105) {
					if(flag == 0 && x == WIDTH - 61) {
						pty += dty;
						y += dty;
					}
					else {
						pty += dty;
					} 
				}
			}
		}
		function checkBallRebond() {
			var id = content.getImageData(x,y,12,12),
			px = id.data;
			for(var i = 0; i < px.length; i+=4) {
				if(px[i+1] == 58) {
					c = 1;
						if(x < (WIDTH / 2)) {
						impact = y - poy;
						calibrateAngle(impact);
						}
						else {
							impact = y - pty;
							calibrateAngle(impact);
						}
				}
			}
		}
/************************************************/
		function calibrateAngle(impact) {
			if(impact < 59 && impact > 49) { 
				dy = -2;
			}
			else if(impact < 50 && impact > 39) {
				dy = -4;
			}
			else if(impact < 40 && impact > 29) {
				dy = -6;
			}
			else if(impact < 30 && impact > 19) {
				dy = -7;
			}
			else if(impact < 20 && impact > 9) {
				dy = -8;
			}
			else if(impact < 10 && impact > -1) {
				dy = -9;
			}
			else if(impact > 62 && impact < 70) {
				dy = 2;
			}
			else if(impact > 69 && impact < 80) {
				dy = 4;
			}
			else if(impact > 79 && impact < 90) {
				dy = 6;
			}
			else if(impact > 89 && impact < 100) {
				dy = 7;
			}
			else if(impact > 99 && impact < 110) {
				dy = 8;
			}
			else if(impact > 109 && impact < 121) {
				dy = 9;
			}
			else {
				dy = 0;
			}
		}
		function miseajourScore() {
			if (x + dx > WIDTH) {
				scores.Joueur1Score++;
				flag = 0;
				pox = 50;
				poy = 50;
				x = 65;
				y = 110;
				dy = 0;
			}
			if (x + dx < 0) {
				scores.Joueur2Score++;
				flag = 0;
				ptx = WIDTH - 50;
				pty = 50;
				x = WIDTH - 61;
				y = 110;
				dy = 0;
				dx = -dx;
			}
		}

		function draw() {
			clear();
			content.fillStyle = '#eee';
			rect(0,0,WIDTH,HEIGHT);
			content.fillStyle = 'rgba(114,58,58,1)';
			content.strokeStyle = 'rgba(120,88,88,1)';
			j1Rect(pox,poy,4,120);
			j2Rect(ptx,pty,4,120);
			content.strokeStyle = '#fff';
			j1Score((WIDTH/4) - 30,HEIGHT/2);
			j2Score(((WIDTH/4) * 3) - 50,HEIGHT/2);
			a == 1 ? content.fillStyle = "#444444" : content.fillStyle = "#b3b3b3";
			circle(x, y, 10);
			miseajourScore();
			flag != 0 ? checkBallRebond() : '';
			if(c == 1) {
				dx = -dx;
				c = 0;
			}
			if(flag == 0) {}
				if(flag == 1) {
					x += dx; y += dy;
				}
				if(y + dy > HEIGHT || y + dy < 0) {
					dy = -dy;
				}	
			}
	
			init();
			window.addEventListener('keydown',onKeyDown,true);
			window.addEventListener('keyup',onKeyUp,true);
		}	
}