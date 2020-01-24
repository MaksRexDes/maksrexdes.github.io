var temp1 = ""
var temp2 = ""
var x;
var y;
var check = true;
var ans = 0;
var map;
function Counter (c) {
	if (check) {
		temp1 += c.innerText;
		document.getElementById("outputCount").innerText = temp1;
	} else {
		temp2 += c.innerText;
		document.getElementById("outputCount").innerText = temp2;
		y = document.getElementById("outputCount").innerText;
	}
}
function Sign (s) {
	if (document.getElementById("outputCount").innerText != 0) {
		check = false;
		map = s.innerText;
		x = document.getElementById("outputCount").innerText;
		document.getElementById("outputCount").innerText = 0;
	}
}
function answer (d) {
	if (map == "+") {
		ans += Number(x) + Number(y);
	}	else if (map == "-") {
		ans = Number(x) - Number(y);
	} else if (map == "*") {
		ans = Number(x) * Number(y);
	} else if (map == "/") {
		ans = Number(x) / Number(y);
	}
	document.getElementById("outputCount").innerText = String(ans);
}
function reset (r) {
	temp1 = ""
	temp2 = ""
	x = "";
	y = "";
	check = true;
	document.getElementById("outputCount").innerText = 0;
}

