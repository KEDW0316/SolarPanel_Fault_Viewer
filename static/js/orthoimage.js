var viewer = OpenSeadragon({
    id: "openseadragon1",
    prefixUrl: "{% static 'img/openseadragon/' %}",
    showNavigator:  true,
    navigatorPosition:   "BOTTOM_LEFT",
    gestureSettingsMouse: { clickToZoom: false},
    tileSources: [{
        type: 'image',
        url:  '{{orthoimage.image.url}}',
        tileOverlap: 1,
        overlays: [
        {% for file in panelfault %}
        {
            id: 'right-arrow-overlay{{file.id}}',
            x: {{file.px_x}},
            y: {{file.px_y}},
            placement: 'BOTTOM',
            checkResize: false
        },
        {% endfor %}
        ],
    }],                                
});

{% for file in panelfault %}
new OpenSeadragon.MouseTracker({
    element: 'right-arrow-overlay{{file.id}}',
    clickHandler: function(e{{file.id}}) {
    
    fault_detail_image({{file.id}})
    }
});
{% endfor %}