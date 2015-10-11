$ ->
  if $("#map.vut").length
    talks =
      lng: 16.596936
      lat: 49.226245

    mapVut = new GMaps {
      div: '#map'
      zoom: 17
      lat: talks.lat
      lng: talks.lng
      scrollwheel: false
      draggable: false
    }

    mapVut.addMarker {
      lat: talks.lat,
      lng: talks.lng,
      title: 'PyCon CZ 2015 - Talks & Keynotes'
    }

  if $("#map.impact").length
    workshops =
      lng: 16.620317
      lat: 49.190492

    mapImpact = new GMaps {
      div: "#map"
      zoom: 15
      lat: workshops.lat
      lng: workshops.lng
      scrollwheel: false
      draggable: false
    }

    mapImpact.addMarker {
      lat: workshops.lat,
      lng: workshops.lng,
      title: 'PyCon CZ 2015 - Sprints & Workshops'
    }
