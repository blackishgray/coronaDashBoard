$(function(){
let linkBtn = $('#drop-link')
	console.log(linkBtn)
	let dropMenu = $('#drop-menu')
	linkBtn.mouseenter(()=>{
		dropMenu.fadeIn(100)

	})
	linkBtn.mouseleave(()=>{
		dropMenu.fadeOut(10000)
	})
})