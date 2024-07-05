$(document).ready(function() {
    // Función para cargar contenido en el div #content
    function loadContent(page) {
        $('#content').load(page, function (response, status, xhr) {
            if (status == "error") {
                $('#content').html("<p>Error al cargar el contenido. Por favor, inténtelo de nuevo.</p>");
            } else {
                if (page == "{% url 'tienda' %}") {
                    loadProductos();
                } else if (page == "{% url 'donaciones' %}") {
                    loadFundaciones(); // Cargar las fundaciones cuando se muestra la página de donaciones
                }
            }
        });
    }

    // Cargar la página de inicio por defecto
    loadContent('{% url 'inicio' %}');

    // Manejar clics en los enlaces del menú y en el carrusel
    $(document).on('click', 'nav a:not([data-categoria]), #carouselExampleIndicators a', function (e) {
        e.preventDefault();
        var page = $(this).attr('href');
        if (page) {
            loadContent(page); // Cargar la página correspondiente al href del enlace
        }
    });

    // Función para cargar productos desde un archivo JSON
    function loadProductos() {
        $.getJSON('{% static 'json/productos.json' %}', function (data) {
            let categoriasHtml = '';
            let productosHtml = '';
            let categorias = {};

            $.each(data.categories, function (key, producto) {
                if (!categorias[producto.idCategory]) {
                    categorias[producto.idCategory] = true;
                    categoriasHtml += `<a class="nav-link" href="#" data-categoria="${producto.idCategory}">${producto.idCategory}</a>`;
                }

                productosHtml += `<div class="card mb-3 col-md-6" style="width: 18rem;" data-categoria="${producto.idCategory}">
                    <img src="${producto.strCategoryThumb}" class="card-img-top" alt="${producto.strCategory}">
                    <div class="card-body">
                        <h5 class="card-title">${producto.strCategory}</h5>
                        <button type="button" class="btn-custom" data-bs-toggle="modal" data-bs-target="#exampleModal${key}">
                            Ver Producto
                        </button>
                        <div class="modal fade" id="exampleModal${key}" tabindex="-1" aria-labelledby="exampleModalLabel${key}" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title fs-5" id="exampleModalLabel${key}">${producto.strCategory}</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <img src="${producto.strCategoryThumb}" class="img-fluid" alt="${producto.strCategory}">
                                        <p>${producto.strCategoryDescription}</p>
                                        <h2>${producto.precioProducto}</h2>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn-custom" data-bs-dismiss="modal">Cerrar</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`;
            });

            $('#categorias').html(categoriasHtml);
            $('#productos').html(productosHtml);

            $('#categorias').on('click', 'a', function (e) {
                e.preventDefault();
                const categoriaSeleccionada = $(this).data('categoria');
                $('.card').hide();
                $(`.card[data-categoria="${categoriaSeleccionada}"]`).show();
            });

            $('.card').show();
        });
    }

    $(document).ready(function() {
        function loadFundaciones() {
            $.getJSON('{% static 'json/organizaciones.json' %}', function (data) {
                let galeriaHtml = '';
                $.each(data.fundaciones, function (key, fundacion) {
                    galeriaHtml += `<div class="col-md-6 mb-4">
                        <div class="card">
                            <img src="${fundacion.imagenFundacion}" class="img-fluid card-img-top" alt="${fundacion.nombreFundacion}" data-bs-toggle="modal" data-bs-target="#orgModal${key}" data-descripcion="${fundacion.descripcionFundacion}">
                            <div class="card-body">
                                <h5 class="card-title">${fundacion.nombreFundacion}</h5>
                                <button class="btn btn-primary subscribe-btn" data-bs-toggle="modal" data-bs-target="#orgModal${key}">Suscribirse</button>
                            </div>
                        </div>
                    </div>`;
                });
                $('#galeria').html(galeriaHtml);
            });
    
            $('#orgModal').on('show.bs.modal', function (event) {
                var button = $(event.relatedTarget);
                var descripcion = button.data('descripcion');
                var modal = $(this);
                modal.find('.modal-body').text(descripcion);
            });
    
            $('#galeria').on('click', '.subscribe-btn', function () {
                var fundacion = $(this).closest('.card-body').find('.card-title').text();
                var donacion = prompt('Ingrese la cantidad de su donación:');
                if (donacion) {
                    alert(`Gracias por su donación de ${donacion} a la ${fundacion}. Recibirá un 5% de descuento en su próxima compra.`);
                }
            });
        }
    
        if ($('#galeria').length) {
            loadFundaciones();
        }
    });
    

    // Función para manejar los botones de filtro de productos de perro y gato
    $('#filter-dog-products').click(function() {
        $('.card').hide();
        $('.card[data-categoria="Perro"]').show();
    });

    $('#filter-cat-products').click(function() {
        $('.card').hide();
        $('.card[data-categoria="Gato"]').show();
    });

    // Mostrar todos los productos inicialmente
    $('.card').show();
});
