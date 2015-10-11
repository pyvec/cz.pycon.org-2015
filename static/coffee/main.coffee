$ ->
  talks =
    lng: 16.596936
    lat: 49.226245

  map = new GMaps {
    div: '#map'
    zoom: 17
    lat: talks.lat
    lng: talks.lng
    scrollwheel: false
    draggable: false
  }

  map.addMarker {
    lat: talks.lat,
    lng: talks.lng,
    title: 'PyCon CZ 2015'
  }
