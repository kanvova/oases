var publications = {
  save: function(id = 0){
    var data = {
      id: id,
      title: $("#edit-publication-title").val(),
      description: $("#edit-publication-description").val(),
      cover: $("#edit-publication-cover").val(),
      author: $("#edit-publication-author").val(),
      content: editor.val()
    }

    if(!data.title){
      $("#edit-publication-title").focus();
      return;
    }

    $.ajax({
      url       : "/publications/save",
      method     : "POST",
      dataType  : "json",
      data      : data
    }).
    done(function(res){
      if(res.status == 'success'){
        location.href = '/publications/' + res.id;
      }
    });
  },
  remove: function(id, confirm = true){
    if(confirm){
      UIkit.modal.confirm('Remove publication?', {
        bgClose: true
      }).then(()=>{
        this.remove(id, false);
        return;
      },function(){});
      return;
    }

    $.ajax({
      url       : "/publications/remove",
      method     : "POST",
      dataType  : "json",
      data      : {id: id}
    }).
    done(function(res){
      if(res.status == 'success'){
        location.href = '/publications';
      }
    });
  },
}

var auth = {
  send: function(){
    var data = {
      login: $("#auth-login").val(),
      password: $("#auth-password").val()
    }

    if(!data.login){
      $("#auth-login").focus();
      return;
    }

    if(!data.password){
      $("#auth-password").focus();
      return;
    }

    $.ajax({
      url       : "/auth/login",
      method     : "POST",
      dataType  : "json",
      data      : data
    }).
    done(function(res){
      if(res.status == 'success'){
        location.reload()
      }
    });
  },
  logout: function(){
    $.ajax({
      url       : "/auth/logout",
      method     : "POST",
      dataType  : "json"
    }).
    done(function(res){
      if(res.status == 'success'){
        location.reload()
      }
    });
  }

}
