$(function () {
   const profile_pic = $(".profile-pic").data("profile_pic")
   const profile_img = profile_pic.split('/').pop()
   console.log(profile_img)

   $.ajax({
       type: 'GET',
       url: `http://127.0.0.1:5001/picture_uploads/${profile_img}`,
       xhrFields: {
	       responseType: 'blob'
       },
       success: function (data) {
	       const imageUrl = URL.createObjectURL(data);
	       console.log(imageUrl)
	       //$(".profile-pic").append(`<img src="${imageUrl}" alt="Profile Picture" style="max-width: 100%; height: auto;">`)
	       $('#profilePicDiv').css('background-image', `url(${imageUrl})`);
               $('#profilePicDiv').css('background-size', 'cover');
               $('#profilePicDiv').css('background-position', 'center'); 
       },
       error: function () {
	       console.log("Image not found");
       }
   });
});

const sidebar = document.querySelector(".sidebar");
const sidebarBtn = document.querySelector(".sidebarBtn");
sidebarBtn.onclick = function() {
    sidebar.classList.toggle("active");
    if (sidebar.classList.contains("active")) {
        sidebarBtn.classList.replace("bx-menu" ,"bx-menu-alt-right");
    } else
    sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
}

dropdownBtn.onclick = function () {
    dropdownContent.style.display = (dropdownContent.style.display === 'block') ? 'none' : 'block';
    dropdownBtn.style.color = (dropdownContent.style.display === 'block') ? 'purple' : ''; 
}