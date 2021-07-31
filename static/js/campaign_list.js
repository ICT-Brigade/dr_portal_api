const url = window.location.origin;
const campaign_modal_body = document.getElementById("campaign-modal-body");

$('#campaign-dtl-modal').on('show.bs.modal', function (e) {
    const cards = [...document.getElementsByClassName("card")];

    cards.forEach(card => card.addEventListener("click", async e => {
        const campaign_id = card.id;
        const {data: data} = await getCampaignByID(campaign_id);
        campaign_modal_body.innerHTML = `
        <div class="container">
            <div class="row">
                <div class="col-md-5" id="modal-campaign-img">
                    <img
                        class="portrait"
                        src="${data.image_link}"
                        alt="Image Unavailable"
                        id="img_${campaign_id}"
                    >
                </div>
                <div class="col-md-7 text-wrap">
                    <h4>
                        <b>${data.source_account}</b>
                    </h4>
                    <p>${data.description}</p>
                    <a
                        class="btn btn-primary"
                        href="${data.link}">
                        DONATE or VOLUNTEER
                    </a>
                </div>
            </div>
        </div>
        `;
        const img = document.getElementById(`img_${campaign_id}`).firstChild;
        if(img) {
            img.onload = function() {
                if(img.height > img.width) {
                    img.height = '100%';
                    img.width = 'auto';
                }
            };
        }
    }));
})

async function getCampaignByID(campaign_id) {
    const headers = new Headers({
        'Accept': 'application/json'
      });
    const req = new Request(`${url}/catalog/api/campaigns/${campaign_id}`, {
        method: 'GET',
        headers,
        mode: 'cors',
        cache: 'default',
    });

    return new Promise(function(ok, not_ok) {
        fetch(req)
        .then(response => response.json())
        .then(json => {
            ok(json);
        });
    });
};