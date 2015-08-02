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
      if location.pathname.replace(/^\//, '') == @pathname.replace(/^\//, '') and location.hostname == @hostname
        target = $(@hash)
        target = if target.length then target else $('[name=' + @hash.slice(1) + ']')
        if target.length
          $('html,body').animate {scrollTop: target.offset().top - 60}, 1000
          return false
      return
    return


$ init
