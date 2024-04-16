
    $.getJSON('/pycall', {content: "content from js"},function(data) {
        alert(data.result);
    });
