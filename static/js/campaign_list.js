const url = window.location.origin;
const default_img = `${url}/static/img/default.png`;
const campaign_modal_body = document.getElementById("campaign-modal-body");


function getById(campaign_id) {
  const dataUrl = `${url}/catalog/api/campaigns/${campaign_id}`;
  $.getJSON(dataUrl, function (json) {
    if (json.success) {
      try {
        const {data: data} = json;
        const img = !data.image_link || data.image_link == "/default.png" ? `${default_img}` : data.image_link;
        const btnLabel = data.campaign_type && data.campaign_type.includes('volunteer') ? "VOLUNTEER" : "DONATE";
        const has_campaign_tag = Boolean(data.campaign_type && data.campaign_type != "");
        const modal_body = `
        <div class="container py-0">
          <div class="row">
            <div class="col-md-5" id="modal-campaign-img">
              <img
                class="portrait"
                src="${img}"
                alt="Image Unavailable"
                id="img_${campaign_id}"
              >
            </div>
            <div class="col-md-7 text-wrap">
              <div class="d-flex flex-row">
                <h4 class="campaign-modal-title">
                  ${data.source_account}
                </h4>
                <div class="px-3">
                  <span class="${has_campaign_tag ? 'px-3 me-auto campaign-modal-tag' : 'd-none'}">${data.campaign_type}</span>
                </div>
              </div>
              <p>${data.description}</p>
              <a class="btn btn-primary dr-btn" href="${data.link}">${btnLabel}</a>
            </div>
          </div>
        </div>`;

        campaign_modal_body.innerHTML = modal_body;
      } catch (error) {
        campaign_modal_body.innerHTML = `
        <div class="container">
        <div class="row">
        <h3>${error.message}</h3>
        </div>
        </div>`;
      }
    }

    // On success show modal
    $('.modal').modal('show');

  });

}
