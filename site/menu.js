let $opcoes = $("nav ul li:nth-child(-n+2)");
let $opcaoSelecionda = $("#descricao-nav");
let $articles = $("main section:last-child article")

$opcoes.click(e => {
    $opcaoSelecionda = $(e.currentTarget);
    $opcoes.removeClass('selecionado');
    $opcaoSelecionda.addClass('selecionado');

    let escolha = $opcaoSelecionda.html();

    $articles.removeClass("visivel")
    if(escolha == "Comandos") {
        $('#comandos').addClass("visivel")
    } else if(escolha == "Apresentação") {
        $('#apresentacao').addClass("visivel")
    }
});