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
