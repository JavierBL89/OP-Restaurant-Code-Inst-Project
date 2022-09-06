// Initialize and add the map
function initMap() {
    // The location of Uluru
    const uluru = { lat: 53.34325646189124, lng: -6.279753565530291 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15,
      center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
    });
  }
  
  window.initMap = initMap;