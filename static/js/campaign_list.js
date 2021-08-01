const url = window.location.origin;
const campaign_modal_body = document.getElementById("campaign-modal-body");


window.onload = function() {
    const cards = [...document.getElementsByClassName("card")];

    cards.forEach(card => card.addEventListener("click", async e => {
        const campaign_id = card.id;
    
        try {
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
                        <h4 class="campaign-modal-title">
                            ${data.campaign_type ? data.source_account + " " +data.campaign_type : data.source_account}
                        </h4>
                        <p>${data.description}</p>
                        <a
                            class="btn btn-primary dr-btn"
                            href="${data.link}">
                            DONATE
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
        } catch (error) {
            console.log(error.message);
            campaign_modal_body.innerHTML = `
            <div class="container">
            <div class="row">
                <h3>${error.message}</h3>
            </div>
        </div>
            `;
        }
    }));
};


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
        .then(response => {
            return response.json();
        })
        .then(json => {
            if (json.success) {
                return ok(json);
            }
            throw Error(json.message)
        })
        .catch(err => {
            not_ok(err)
        });
    });
};