document.addEventListener('DOMContentLoaded', function() {
  /*===== LINK ACTIVE  =====*/
  let linkColor = document.querySelectorAll('.nav__link');
  function colorLink() {
    linkColor.forEach(l => l.classList.remove('active'));
    this.classList.add('active');
  }
  linkColor.forEach(l => l.addEventListener('click', colorLink));

  /*===== COLLAPSE MENU  =====*/
  const linkCollapse = document.querySelectorAll('.collapse__link');
  linkCollapse.forEach(function(collapseLink) {
    collapseLink.addEventListener('click', function() {
      const collapseMenu = this.nextElementSibling;
      collapseMenu.classList.toggle('showCollapse');

      const rotateIcon = this.querySelector('.collapse__icon');
      rotateIcon.classList.toggle('rotate');
    });
  });

  // Button and Table Show/Hide
  $('#mmeBtn').click(function(e) {
    e.preventDefault();
    $('.mme-section').hide();
    $('#mmeContainer').show();
  });

  $('#intBtn').click(function(e) {
    e.preventDefault();
    const intVisible = $('#intContainer').is(':visible');
    if (!intVisible) {
      $('.mme-section').hide();
      $('#intContainer').show();
    }
  });

  $('#globalBtn').click(function(e) {
    e.preventDefault();
    const globalVisible = $('#globalContainer').is(':visible');
    if (!globalVisible) {
      $('.mme-section').hide();
      $('#mmeContainer').hide();
      $('#globalContainer').show();
    }
  });

  $('#epgBtn').click(function(e) {
    e.preventDefault();
    const epgVisible = $('#epgContainer').is(':visible');
    if (!epgVisible) {
      $('.mme-section').hide();
      $('#epgContainer').show();
    }
  });

  $('.nav__link').not('#mmeBtn, #intBtn, #globalBtn').click(function() {
    $('.mme-section').hide();
  });

  // Go Button Click
  $('#goBtn').click(function(e) {
    e.preventDefault();
    const selectedOption = $('.custom-select').val();
    $('.table-section').hide();
    $('#' + selectedOption.toLowerCase() + '_table').show();
  });

  // Initialize Swiper
  var swiper = new Swiper('.swiper-container', {
    // Optional parameters
    loop: true,

    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
});

