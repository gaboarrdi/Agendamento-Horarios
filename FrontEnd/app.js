// Criar a funçao que permite abertura e fechamento do PopUp//

function clicou() {
    const remover = document.getElementById("popup");
    remover.classList.remove("visual");
}

function voltar() {
    const retornar = document.getElementById("popup");
    retornar.classList.add("visual");
}

//Enviando cadastro para o back-end //
function fazPost(url, body) {
    console.log("Body=", body)
    let request = new XMLHttpRequest()
    request.open("POST", url, true)
    request.setRequestHeader("Content-type", "application/json")
    request.send(JSON.stringify(body))

    request.onload = function() {
        console.log(this.responseText)
        alert("Você reservou um horário!")
    }

    return request.responseText
}


function cadastraReserva() {
    event.preventDefault()
    let url = "http://127.0.0.1:8000/reservas/"
    let nome = document.getElementById("FormNome").value
    let dia = document.getElementById("FormDia").value
    let periodo = document.getElementById("FormPeriodo").value
    let mesa = document.getElementById("FormMesa").value

    console.log(nome)
    console.log(dia)
    console.log(periodo)
    console.log(mesa)

    body = {
        "nome": nome,
        "dia": dia,
        "periodo": periodo,
        "mesa": mesa

    }

    fazPost(url, body )
}


/* Apresentar Informações do Banco de Dados de Reservas */
function fazGet(url) {
    let request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send()
    return request.responseText
}

function criaCard(usuario) {
    console.log(usuario)
    linha = document.createElement("tr");
    pNome = document.createElement("td");
    pDia = document.createElement("td");
    pPeriodo = document.createElement("td");
    pMesa = document.createElement("td");
    vazio = document.createElement("br")
    
    pNome.innerHTML = usuario.nome;
    pDia.innerHTML = usuario.dia;
    pPeriodo.innerHTML = usuario.periodo;
    pMesa.innerHTML = usuario.mesa

    linha.appendChild(pNome);
    linha.appendChild(pDia);
    linha.appendChild(pPeriodo);
    linha.appendChild(pMesa);

    return linha;
}

function main() {
   let data = fazGet("http://127.0.0.1:8000/reservas/")
    let reservas = JSON.parse(data);
    console.log(reservas);
    let card = document.getElementById("tabela")

    reservas.forEach(element => {
        let linha = criaCard(element);
        card.appendChild(linha);
    });
}

main()

 
 



