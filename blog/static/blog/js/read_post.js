$(document).ready(function () {
    function submitComment() {

      // Get the form data
      var post_id = $("#comment-form").data("post-id");
      var formData = $("#comment-form").serialize();

      // URL for AJAX request
      var url = "/read_post/" + post_id;

      $.ajax({
        type: "POST",
        url: url,
        data: formData,
        success: function (data) {

          // clear the form
          $("#comment-form")[0].reset();

          // insert new comment before first child
          var newComment = $(data.comment_html);
          newComment.find('div:first').addClass("new-comment");
          $(".comments-container").children().first().before(newComment);

          // display success mage
        },
        error: function (error) {
          // display error message
          console.log("error", error);
        }
      });
    }

    function deleteComment(commentId) {
      var url = "/delete_comment/" + commentId;

      $.ajax({
        type: 'DELETE',
        url: url,
        data: {},
        success: function (response) {
          if (response.message === 'OK') {
            $(`#comment-${commentId}`).remove();
          }
          else {
            alert('Ssdasd.');
          }
        },
        error: function () {
          alert('Something went wrong.');
        }
      });
    }

    $("#comment-form").submit(function(e) {
      e.preventDefault();
      submitComment();
    });

    $(document).on('click', '.delete-comment', function () {
      var commentId = $(this).data('comment-id');
      deleteComment(commentId);
    });
  });