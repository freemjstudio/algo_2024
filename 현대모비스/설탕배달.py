< script
src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js" > < / script >

< script
type = "text/javascript" >
$(document).ready(function()
{
$('h1,h2,h3,h4,p,span').removeAttr('data-ke-size').css('color', '');;
});
< / script >
< script >
document.addEventListener("DOMContentLoaded", function()
{

// Remove & nbsp; and & gt;
from HTML content

var
allElements = document.querySelectorAll("*");

for (var i = 0; i < allElements.length; i++)
{
    var
element = allElements[i];
var
htmlContent = element.innerHTML;

// Replace & nbsp; with space
htmlContent = htmlContent.replace( / & nbsp; / g, ' ');

// Replace & gt; with >
htmlContent = htmlContent.replace( / & gt; / g, '>');

element.innerHTML = htmlContent;
}
});
< / script >