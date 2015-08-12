lng = 16.596936
lat = 49.226245


init = () ->
  map = new GMaps {
    div: '#map'
    zoom: 17
    lat: lat
    lng: lng
    scrollwheel: false
  }

  map.addMarker {
    lat: lat,
    lng: lng,
    title: 'PyCon CZ 2015'
  }


  $ ->
    $('a[href*=#]:not([href=#])').click ->
      p_name = location.pathname
      l_cond = p_name.replace(/^\//, '') == @pathname.replace(/^\//, '')
      if l_cond and location.hostname == @hostname
        target = $(@hash)
        if not target.length
          target = $('[name=' + @hash.slice(1) + ']')
        if target.length
          $('html,body').animate {scrollTop: target.offset().top - 60}, 300
          return false
      return
    return


$ init
