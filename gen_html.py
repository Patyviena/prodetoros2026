html = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>Prode Toros 2026</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs@2.0.8/hammer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom@2.0.1/dist/chartjs-plugin-zoom.min.js"></script>
<style>
:root{--bg:#0d1117;--bg-card:#161b22;--bg-card2:#1c2128;--border:#30363d;--cyan:#00e5ff;--pink:#ff4081;--violet:#b388ff;--green:#3fb950;--text:#e6edf3;--muted:#7d8590;--gold:#ffd700;--gold2:#ff9500;--silver:#c0c0c0;--bronze:#cd7f32;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--text);display:flex;height:100vh;overflow:hidden;}
.sidebar{width:230px;flex-shrink:0;background:var(--bg-card);border-right:1px solid var(--border);display:flex;flex-direction:column;height:100vh;position:fixed;left:0;top:0;z-index:100;}
.sidebar-brand{padding:22px 20px 18px;border-bottom:1px solid rgba(255,215,0,.18);background:linear-gradient(180deg,rgba(255,215,0,.04) 0%,transparent 100%);}
.brand-label{font-size:.62rem;font-weight:700;color:var(--gold);letter-spacing:2.5px;text-transform:uppercase;margin-bottom:4px;}
.brand-title{font-size:1.4rem;font-weight:800;background:linear-gradient(135deg,var(--text) 30%,var(--gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;}
.sidebar-nav{padding:10px 0;flex:1;overflow-y:auto;}
.nav-section{padding:14px 20px 6px;font-size:.58rem;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--muted);}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 20px;color:var(--muted);font-size:.88rem;font-weight:500;transition:all .15s;cursor:pointer;border:none;border-left:3px solid transparent;background:none;width:100%;text-align:left;}
.nav-item:hover{color:var(--text);background:rgba(255,255,255,.04);}
.nav-item.active{color:var(--gold);border-left-color:var(--gold);background:rgba(255,215,0,.05);}
.nav-item.calc-nav.active{color:var(--gold);border-left-color:var(--gold);background:rgba(255,215,0,.05);}
.nav-item.relator-nav.active{color:var(--pink);border-left-color:var(--pink);background:rgba(255,64,129,.05);}
.nav-icon{font-size:.9rem;width:18px;text-align:center;flex-shrink:0;}
.nav-divider{height:1px;background:var(--border);margin:8px 0;}
.sidebar-footer{padding:16px 20px;border-top:1px solid var(--border);}
.footer-updated{font-size:.63rem;color:var(--muted);line-height:1.5;margin-bottom:10px;}
.leader-card{background:linear-gradient(135deg,rgba(255,215,0,.09),rgba(255,149,0,.05));border:1px solid rgba(255,215,0,.28);border-radius:10px;padding:13px 14px;animation:goldPulse 3s ease-in-out infinite;}
@keyframes goldPulse{0%,100%{border-color:rgba(255,215,0,.28);}50%{border-color:rgba(255,215,0,.55);box-shadow:0 0 12px rgba(255,215,0,.1);}}
.leader-tag{font-size:.57rem;font-weight:700;text-transform:uppercase;letter-spacing:1.8px;color:var(--gold);margin-bottom:8px;}
.leader-name-row{display:flex;align-items:center;gap:7px;font-size:.93rem;font-weight:700;color:var(--text);margin-bottom:3px;}
.leader-pts-row{font-size:.72rem;color:var(--muted);margin-bottom:2px;padding-left:16px;}
.leader-gap{font-size:.7rem;color:var(--gold2);padding-left:16px;margin-bottom:10px;font-weight:500;}
.leader-prize{display:flex;align-items:center;gap:6px;font-size:.76rem;font-weight:700;color:var(--gold);border-top:1px solid rgba(255,215,0,.15);padding-top:8px;margin-top:2px;letter-spacing:.3px;}
.main-content{margin-left:230px;flex:1;height:100vh;overflow-y:scroll;scrollbar-width:none;}
.main-content::-webkit-scrollbar{display:none;}
.content-section{padding:52px 48px;border-bottom:1px solid var(--border);}
.content-section:last-child{border-bottom:none;padding-bottom:80px;}
.section-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:32px;gap:16px;}
.section-title{font-size:1.15rem;font-weight:700;color:var(--text);display:flex;align-items:center;gap:10px;}
.section-bar{width:3px;height:18px;background:var(--gold);border-radius:2px;flex-shrink:0;}
.section-desc{font-size:.76rem;color:var(--muted);margin-top:5px;padding-left:19px;}
.rank-table{width:100%;border-collapse:collapse;}
.rank-table th{padding:8px 14px;text-align:right;font-size:.67rem;text-transform:uppercase;letter-spacing:1px;color:var(--muted);border-bottom:1px solid var(--border);font-weight:600;white-space:nowrap;}
.rank-table th:nth-child(2){text-align:left;}
.rank-table td{padding:12px 14px;border-bottom:1px solid rgba(48,54,61,.5);text-align:right;vertical-align:middle;}
.rank-table tbody tr{transition:background .1s;}
.rank-table tbody tr:hover td{background:rgba(255,255,255,.025);}
.rk-pos{font-size:.82rem;font-weight:700;color:var(--muted);text-align:center;width:32px;}
.rk-pos.p1{color:var(--gold);}
.rk-pos.p2{color:var(--silver);}
.rk-pos.p3{color:var(--bronze);}
.rk-name{display:flex;align-items:center;gap:10px;font-weight:500;font-size:.91rem;text-align:left;}
.clr-dot{width:9px;height:9px;border-radius:50%;flex-shrink:0;}
.rk-pts{font-weight:700;font-size:1rem;}
.rk-pts.p1{color:var(--gold);}
.rk-pts.p2{color:var(--silver);}
.rk-pts.p3{color:var(--bronze);}
.rk-stat{font-size:.88rem;color:var(--muted);font-variant-numeric:tabular-nums;}
.rk-stat.gold{color:var(--gold);font-weight:600;}
.rk-stat.gold2{color:var(--gold2);font-weight:600;}
.rk-win{font-size:.88rem;font-variant-numeric:tabular-nums;font-weight:600;color:var(--muted);}
.rk-win-hi{color:var(--gold);}
.rk-win-mid{color:var(--gold2);}
.rk-win-lo{color:var(--border);font-weight:400;}
.rk-form{display:flex;gap:3px;justify-content:flex-end;}
.rk-form-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;}
.rk-form-dot.miss{background:var(--border);}
.rk-form-dot.common{background:var(--green);}
.rk-form-dot.exact{background:var(--gold);}
.rk-form-dot.bonus{background:var(--gold2);}
.chart-outer{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:20px;height:520px;position:relative;}
.chart-mobile-legend{display:none;}
.reset-zoom-btn{background:rgba(255,215,0,.07);border:1px solid rgba(255,215,0,.3);color:var(--gold);border-radius:6px;padding:6px 14px;font-size:.73rem;cursor:pointer;transition:all .2s;letter-spacing:.5px;white-space:nowrap;}
.reset-zoom-btn:hover{background:rgba(255,215,0,.14);}
.bracket-wrap{overflow-x:auto;padding-bottom:8px;scrollbar-width:thin;scrollbar-color:var(--border) transparent;}.bracket-wrap::-webkit-scrollbar{height:5px;}.bracket-wrap::-webkit-scrollbar-track{background:transparent;}.bracket-wrap::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}.bracket-wrap::-webkit-scrollbar-thumb:hover{background:var(--muted);}
.bracket{display:flex;align-items:stretch;position:relative;height:860px;gap:24px;min-width:max-content;padding:0 4px;}
.br-col{display:flex;flex-direction:column;width:172px;flex-shrink:0;}
.br-col-header{text-align:center;padding:0 4px 12px;font-size:.61rem;font-weight:700;text-transform:uppercase;letter-spacing:1.8px;}
.br-slots{flex:1;display:flex;flex-direction:column;justify-content:space-around;}
.bm{background:var(--bg-card2);border:1px solid var(--border);border-radius:8px;padding:9px 11px;transition:all .15s;user-select:none;display:flex;flex-direction:column;gap:3px;}
.bm.tbd{opacity:.28;border-style:dashed;}
.bm.locked{border-style:dashed;border-color:rgba(125,133,144,.35);}
.bm.locked .bm-match{color:var(--muted);}
.bm-lock{font-size:.72rem;color:var(--muted);margin-top:4px;opacity:.6;}
.bm.clickable{cursor:pointer;border-color:rgba(255,215,0,.22);}
.bm.clickable:hover{background:rgba(255,215,0,.07);border-color:rgba(255,215,0,.6);transform:translateY(-1px);box-shadow:0 4px 14px rgba(255,215,0,.1);}
.bm.selected{background:rgba(255,215,0,.12);border-color:var(--gold);box-shadow:0 0 0 1px rgba(255,215,0,.25);}
.bm.played{border-color:rgba(63,185,80,.28);}
.bm.played.clickable:hover{border-color:var(--green);background:rgba(63,185,80,.07);}
.bm.played.selected{background:rgba(63,185,80,.1);border-color:var(--green);}
.bm-final{border-color:rgba(255,215,0,.35)!important;}
.bm-3rd{border-color:rgba(179,136,255,.3)!important;}
.bm-id{font-size:.57rem;color:var(--muted);}
.bm-match{font-size:.73rem;font-weight:600;line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:150px;}
.bm-match.tbd-name{color:var(--muted);font-weight:400;}
.bm-dots{display:flex;gap:3px;margin-top:3px;}
.bd{width:5px;height:5px;border-radius:50%;background:var(--border);}
.bd.on{background:var(--gold);}
.bd.on.played{background:var(--green);}
#bracket-svg{position:absolute;top:0;left:0;pointer-events:none;overflow:visible;}
.pred-detail{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:28px;margin-top:24px;display:none;animation:fadeIn .2s;}
.pred-detail.open{display:block;}
@keyframes fadeIn{from{opacity:0;transform:translateY(-6px);}to{opacity:1;transform:none;}}
.pred-head{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:20px;gap:16px;}
.pred-match-name{font-size:1.1rem;font-weight:700;margin-bottom:3px;}
.pred-match-meta{font-size:.74rem;color:var(--muted);}
.pred-close{background:none;border:1px solid var(--border);color:var(--muted);border-radius:6px;padding:5px 12px;font-size:.74rem;cursor:pointer;transition:all .15s;white-space:nowrap;}
.pred-close:hover{color:var(--text);border-color:var(--text);}
.pred-summary{display:flex;gap:16px;margin-bottom:20px;flex-wrap:wrap;}
.psum{font-size:.8rem;color:var(--muted);display:flex;align-items:center;gap:6px;}
.psum-dot{width:8px;height:8px;border-radius:50%;}
.pred-groups{display:flex;flex-wrap:wrap;gap:10px;}
.pg{background:var(--bg-card2);border:1px solid var(--border);border-radius:8px;padding:12px 14px;min-width:120px;}
.pg-score{font-size:1.05rem;font-weight:700;margin-bottom:2px;}
.pg-score.local{color:var(--gold);}
.pg-score.away{color:var(--pink);}
.pg-score.tie{color:var(--violet);}
.pg-count{font-size:.67rem;color:var(--muted);margin-bottom:5px;}
.pg-names{font-size:.7rem;color:var(--text);line-height:1.6;}
.legend-row{display:flex;gap:18px;flex-wrap:wrap;margin-bottom:24px;}
.legend-item{display:flex;align-items:center;gap:6px;font-size:.7rem;color:var(--muted);}
.legend-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.sim-content{margin-left:230px;flex:1;height:100vh;display:flex;flex-direction:column;overflow-y:auto;}
.sim-header{padding:28px 40px 20px;border-bottom:1px solid var(--border);flex-shrink:0;display:flex;align-items:flex-start;justify-content:space-between;gap:20px;}
.sim-title-block{}
.sim-title{font-size:1.15rem;font-weight:700;display:flex;align-items:center;gap:10px;margin-bottom:4px;}
.sim-subtitle{font-size:.76rem;color:var(--muted);}
.sim-bonus-note{font-size:.68rem;color:var(--muted);margin-top:3px;font-style:italic;}
.sim-reset-btn{background:rgba(179,136,255,.08);border:1px solid rgba(179,136,255,.3);color:var(--violet);border-radius:6px;padding:7px 16px;font-size:.73rem;cursor:pointer;transition:all .2s;white-space:nowrap;flex-shrink:0;}
.sim-reset-btn:hover{background:rgba(179,136,255,.15);}
.sim-body{flex:1;display:flex;overflow:hidden;}
.sim-left{width:380px;flex-shrink:0;overflow-y:scroll;padding:20px 24px 32px;border-right:1px solid var(--border);scrollbar-width:none;}
.sim-left::-webkit-scrollbar{display:none;}
.sim-right{flex:1;overflow-y:scroll;padding:20px 40px 32px;scrollbar-width:none;}
.sim-right::-webkit-scrollbar{display:none;}
.sim-right-header{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--muted);margin-bottom:16px;}
.sim-phase-lbl{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin-bottom:8px;margin-top:22px;display:flex;align-items:baseline;gap:8px;}
.sim-phase-lbl:first-child{margin-top:0;}
.sim-phase-pts{font-weight:400;color:var(--muted);font-size:.57rem;letter-spacing:0;}
.sim-card{background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:13px 14px;margin-bottom:8px;transition:border-color .15s;}
.sim-card.has-score{border-color:rgba(255,215,0,.3);}
.sim-card-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;}
.sim-card-name{font-size:.82rem;font-weight:600;line-height:1.3;flex:1;}
.sim-card-id{font-size:.6rem;color:var(--muted);flex-shrink:0;padding-top:1px;}
.sim-score-row{display:flex;align-items:center;gap:8px;}
.sim-inp{width:44px;height:38px;background:var(--bg-card2);border:1px solid var(--border);border-radius:7px;color:var(--text);font-size:1.1rem;font-weight:700;text-align:center;outline:none;transition:border-color .15s;}
.sim-inp:focus{border-color:var(--cyan);}
.sim-inp::-webkit-inner-spin-button,.sim-inp::-webkit-outer-spin-button{-webkit-appearance:none;}
.sim-sep{font-size:1.1rem;font-weight:700;color:var(--muted);user-select:none;}
.sim-ok{font-size:.68rem;color:var(--green);margin-left:8px;opacity:0;transition:opacity .2s;}
.sim-card.has-score .sim-ok{opacity:1;}
.sim-pred-cnt{font-size:.63rem;color:var(--muted);margin-top:6px;}
.sim-rank-row{display:grid;grid-template-columns:32px 1fr 48px 44px 44px 52px 54px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(48,54,61,.4);gap:4px;}
.sim-rank-row:last-child{border-bottom:none;}
.sim-rank-pos{font-size:.82rem;font-weight:700;color:var(--muted);text-align:center;}
.sim-rank-pos.p1{color:var(--gold);}
.sim-rank-pos.p2{color:var(--silver);}
.sim-rank-pos.p3{color:var(--bronze);}
.sim-rank-name{display:flex;align-items:center;gap:8px;font-size:.88rem;font-weight:500;}
.sim-rank-num{font-size:.85rem;text-align:right;color:var(--muted);}
.sim-rank-total{font-size:.95rem;font-weight:700;text-align:right;}
.sim-rank-total.p1{color:var(--gold);}
.sim-rank-total.p2{color:var(--silver);}
.sim-rank-total.p3{color:var(--bronze);}
.sim-rank-delta{font-size:.78rem;text-align:right;font-weight:600;}
.sim-rank-header{display:grid;grid-template-columns:32px 1fr 60px 60px 70px 40px;padding:0 0 8px;border-bottom:1px solid var(--border);gap:4px;margin-bottom:4px;}
.sim-rank-header span{font-size:.63rem;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);font-weight:600;text-align:right;}
.sim-rank-header span:nth-child(2){text-align:left;}
.sim-cls-row{display:flex;align-items:center;gap:5px;margin-top:8px;}
.sim-cls-lbl{font-size:.62rem;color:var(--muted);white-space:nowrap;}
.sim-cls-btn{background:none;border:1px solid var(--border);color:var(--muted);border-radius:5px;padding:3px 9px;font-size:.67rem;cursor:pointer;transition:all .15s;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:110px;}
.sim-cls-btn:hover{border-color:var(--gold);color:var(--gold);}
.sim-cls-btn.active{background:rgba(255,215,0,.1);border-color:var(--gold);color:var(--gold);font-weight:600;}
.pg-classif{font-size:.65rem;color:var(--gold);margin-left:4px;}
.finale-banner{background:linear-gradient(135deg,rgba(255,215,0,.09),rgba(255,149,0,.04));border:1px solid rgba(255,215,0,.25);border-radius:8px;padding:9px 12px;margin-bottom:10px;text-align:center;animation:goldPulse 3s ease-in-out infinite;}
.finale-banner-title{font-size:.62rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:2px;}
.finale-banner-sub{font-size:.58rem;color:var(--muted);}
.relator-content{margin-left:230px;flex:1;height:100vh;display:flex;flex-direction:column;overflow:hidden;}
/* Seccion Fases y Bonus (feed principal) */
.phase-tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:28px;}
.phase-tab{padding:6px 16px;border-radius:20px;font-size:.73rem;font-weight:600;border:1px solid var(--border);background:none;color:var(--muted);cursor:pointer;transition:all .15s;white-space:nowrap;}
.phase-tab:hover{color:var(--text);border-color:var(--muted);}
.phase-tab.active{background:var(--gold);color:var(--bg);border-color:var(--gold);}
.phase-tab.done{border-color:var(--green);}
.phase-tab.done.active{background:var(--green);color:var(--bg);border-color:var(--green);}
.phase-tab.upcoming{opacity:.4;}
.phase-badge{font-size:.55rem;vertical-align:super;margin-left:3px;font-weight:700;}
.phase-content{display:none;}.phase-content.active{display:block;}
.phase-lead-title{font-size:.68rem;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);font-weight:700;margin-bottom:12px;}
.phase-row{display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid rgba(48,54,61,.4);}
.phase-row:last-child{border-bottom:none;}
.phase-pos{width:22px;text-align:center;font-size:.75rem;color:var(--muted);font-weight:700;flex-shrink:0;}
.phase-pos.p1{color:var(--gold);}
.phase-pos.p2{color:var(--silver);}
.phase-pos.p3{color:var(--bronze);}
.phase-name{width:150px;font-size:.84rem;display:flex;align-items:center;gap:7px;flex-shrink:0;}
.phase-pts-val{width:36px;text-align:right;font-weight:700;font-variant-numeric:tabular-nums;font-size:.9rem;flex-shrink:0;}
.phase-bar-wrap{flex:1;height:7px;background:var(--border);border-radius:4px;overflow:hidden;}
.phase-bar-fill{height:100%;border-radius:4px;transition:width .4s ease;}
.phase-upcoming-msg{color:var(--muted);font-size:.85rem;padding:24px 0;text-align:center;}
.day-group{margin-top:28px;}
.day-header{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);padding-bottom:8px;border-bottom:1px solid var(--border);margin-bottom:10px;display:flex;align-items:center;gap:10px;}
.day-match-row{display:flex;align-items:baseline;gap:8px;padding:5px 0;border-bottom:1px solid rgba(48,54,61,.3);font-size:.8rem;}
.day-match-name{color:var(--muted);min-width:180px;}
.day-match-scores{display:flex;gap:6px;flex-wrap:wrap;}
.day-score-chip{font-size:.7rem;font-variant-numeric:tabular-nums;padding:1px 6px;border-radius:3px;font-weight:600;}
.dsc-exact{background:rgba(63,185,80,.15);color:#3fb950;}
.dsc-common{background:rgba(0,229,255,.1);color:var(--cyan);}
.dsc-bonus{background:rgba(255,215,0,.15);color:var(--gold);}
.dsc-miss{background:rgba(48,54,61,.6);color:var(--muted);}
/* Bonus section */
.bonus-intro{font-size:.8rem;color:var(--muted);margin-bottom:24px;line-height:1.7;}
.bonus-row{display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid rgba(48,54,61,.4);}
.bonus-row:last-child{border-bottom:none;}
.bonus-pos{width:22px;text-align:center;font-size:.75rem;color:var(--muted);font-weight:700;flex-shrink:0;}
.bonus-pos.p1{color:var(--gold);}
.bonus-pos.p2{color:var(--silver);}
.bonus-pos.p3{color:var(--bronze);}
.bonus-name{width:150px;font-size:.84rem;display:flex;align-items:center;gap:7px;flex-shrink:0;}
.bonus-total{width:48px;text-align:right;font-weight:700;font-variant-numeric:tabular-nums;font-size:.95rem;flex-shrink:0;}
.bonus-chips{display:flex;gap:5px;flex-wrap:wrap;}
.bonus-chip{font-size:.65rem;padding:2px 7px;border-radius:10px;border:1px solid rgba(255,215,0,.25);color:var(--gold2);background:rgba(255,215,0,.07);white-space:nowrap;}
.bonus-zero{color:var(--border);font-size:.75rem;}
/* Paneles herramientas adicionales (compartido) */
.tool-content{margin-left:230px;flex:1;height:100vh;display:flex;flex-direction:column;overflow:hidden;}
.tool-header{padding:28px 48px 20px;border-bottom:1px solid var(--border);flex-shrink:0;}
.tool-title{font-size:1.3rem;font-weight:700;display:flex;align-items:center;gap:10px;margin-bottom:4px;}
.tool-subtitle{font-size:.82rem;color:var(--muted);}
.tool-body{flex:1;overflow-y:scroll;padding:28px 40px 60px;scrollbar-width:none;}
.tool-body::-webkit-scrollbar{display:none;}
/* Badges */
.badges-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;}
.badge-card{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:20px 22px;display:flex;flex-direction:column;gap:6px;transition:border-color .2s;}
.badge-card:hover{border-color:var(--gold);}
.badge-icon{font-size:1.8rem;line-height:1;}
.badge-title{font-size:.95rem;font-weight:700;margin-top:4px;}
.badge-desc{font-size:.75rem;color:var(--muted);line-height:1.5;}
.badge-winner{font-size:1rem;font-weight:700;margin-top:8px;}
.badge-stat{font-size:.78rem;color:var(--muted);}
.badges-section-lbl{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:28px 0 14px;display:flex;align-items:center;gap:8px;}
.badges-section-lbl:first-child{margin-top:0;}
.badges-section-lbl.ko{color:var(--gold);}
.badges-section-sub{font-weight:400;text-transform:none;letter-spacing:0;font-size:.7rem;color:var(--muted);}
.badge-card.ko-badge{border-color:rgba(255,215,0,.15);}
.badge-card.ko-badge:hover{border-color:var(--gold);}
.dif-section-lbl{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:28px 0 14px;}
.dif-section-lbl.ko{color:var(--gold);}
.matrix-phase-hdr{padding:8px 0 4px!important;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);text-align:left!important;background:var(--bg)!important;border-bottom:1px solid var(--border)!important;}
.matrix-phase-hdr.ko{color:var(--gold);}
/* Matriz de predicciones */
.matrix-wrap{overflow-x:auto;scrollbar-width:thin;scrollbar-color:var(--border) transparent;}
.matrix-wrap::-webkit-scrollbar{height:5px;}
.matrix-wrap::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}
.matrix-table{border-collapse:collapse;font-size:.72rem;min-width:100%;}
.matrix-table th{position:sticky;top:0;background:var(--bg-card);padding:6px 4px;text-align:center;border-bottom:2px solid var(--border);white-space:nowrap;font-weight:600;z-index:2;}
.matrix-match-col{text-align:left!important;min-width:160px;position:sticky;left:0;z-index:3!important;background:var(--bg-card)!important;}
.matrix-res-col{min-width:54px;}
.matrix-player-col{min-width:48px;font-size:.65rem;}
.matrix-table td{padding:4px;text-align:center;border-bottom:1px solid rgba(48,54,61,.5);}
.matrix-match-name{text-align:left!important;color:var(--muted);font-size:.7rem;position:sticky;left:0;background:var(--bg);z-index:1;padding:4px 8px 4px 0!important;}
.matrix-actual{font-weight:600;color:var(--text);}
.matrix-cell{border-radius:4px;font-variant-numeric:tabular-nums;}
.mx-exact{background:rgba(63,185,80,.18);color:#3fb950;font-weight:700;}
.mx-common{background:rgba(255,215,0,.12);color:var(--gold);}
.mx-miss{background:rgba(255,64,129,.08);color:rgba(255,64,129,.6);}
tr.diff-hard .matrix-match-name{color:var(--pink);}
tr.diff-med .matrix-match-name{color:var(--gold2);}
.matrix-legend{display:flex;gap:16px;margin-bottom:16px;font-size:.75rem;flex-wrap:wrap;}
.mx-leg{display:flex;align-items:center;gap:6px;}
.mx-leg-dot{width:10px;height:10px;border-radius:3px;}
/* Dificultad */
.dif-table{width:100%;border-collapse:collapse;font-size:.82rem;}
.dif-table th{padding:8px 10px;text-align:left;border-bottom:2px solid var(--border);font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);}
.dif-table td{padding:7px 10px;border-bottom:1px solid rgba(48,54,61,.5);}
.dif-match{color:var(--text);font-weight:500;}
.dif-result{font-variant-numeric:tabular-nums;color:var(--muted);}
.dif-num{text-align:center;font-variant-numeric:tabular-nums;font-weight:600;}
.dif-bar-cell{display:flex;align-items:center;gap:10px;min-width:200px;}
.dif-bar{flex:1;height:6px;background:var(--border);border-radius:3px;overflow:hidden;}
.dif-fill{height:100%;background:var(--pink);border-radius:3px;transition:width .3s;}
.dif-label{font-size:.72rem;white-space:nowrap;color:var(--muted);}
.dif-rank-badge{display:inline-block;width:22px;height:22px;border-radius:50%;background:var(--border);font-size:.65rem;font-weight:700;text-align:center;line-height:22px;color:var(--muted);}
.relator-header{padding:28px 48px 20px;border-bottom:1px solid var(--border);flex-shrink:0;display:flex;align-items:flex-start;justify-content:space-between;gap:20px;}
.relator-title{font-size:1.15rem;font-weight:700;display:flex;align-items:center;gap:10px;margin-bottom:5px;}
.relator-subtitle{font-size:.76rem;color:var(--muted);}
.relator-btn{background:rgba(255,64,129,.08);border:1px solid rgba(255,64,129,.35);color:var(--pink);border-radius:6px;padding:7px 16px;font-size:.73rem;cursor:pointer;transition:all .2s;white-space:nowrap;flex-shrink:0;}
.relator-btn:hover{background:rgba(255,64,129,.15);}
.relator-body{flex:1;overflow-y:scroll;padding:36px 64px 60px;scrollbar-width:none;max-width:820px;}
.relator-body::-webkit-scrollbar{display:none;}
.relator-line{padding:16px 20px 16px 22px;margin-bottom:12px;border-left:3px solid var(--border);border-radius:0 8px 8px 0;background:var(--bg-card);font-size:.93rem;line-height:1.8;animation:slideRelator .35s ease both;}
.relator-line:first-child{border-left-color:var(--gold);font-size:1.06rem;font-weight:600;background:rgba(255,215,0,.05);}
.relator-line:last-child{border-left-color:var(--gold);background:rgba(255,215,0,.04);font-style:italic;}
@keyframes slideRelator{from{opacity:0;transform:translateX(-10px);}to{opacity:1;transform:none;}}
#loading{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:var(--bg);gap:12px;font-size:.95rem;color:var(--muted);}
.spinner{width:24px;height:24px;border:2.5px solid var(--border);border-top-color:var(--gold);border-radius:50%;animation:spin .7s linear infinite;}
@keyframes spin{to{transform:rotate(360deg);}}
/* Section dots */
.s-dots{position:fixed;right:18px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:11px;z-index:50;}
.s-dot{width:9px;height:9px;border-radius:50%;background:var(--border);border:none;padding:0;cursor:pointer;transition:all .22s;}
.s-dot.active{background:var(--gold);transform:scale(1.45);}
.s-dot:hover:not(.active){background:var(--muted);}
/* Sim lock */
.sim-content{position:relative;}
.sim-lock-overlay{position:absolute;inset:0;z-index:30;background:rgba(13,17,23,.97);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;text-align:center;padding:48px;pointer-events:all;}
.sim-lock-icon{font-size:3.2rem;line-height:1;}
.sim-lock-title{font-size:1.15rem;font-weight:700;}
.sim-lock-desc{font-size:.85rem;color:var(--muted);max-width:320px;line-height:1.75;}
.bm-result{font-size:.72rem;font-weight:700;color:var(--green);margin-top:3px;letter-spacing:.3px;}
.sim-random-btn{background:rgba(179,136,255,.1);border:1px solid rgba(179,136,255,.3);color:var(--violet);border-radius:8px;padding:8px 14px;font-size:.8rem;font-weight:600;cursor:pointer;margin-right:8px;transition:all .2s;letter-spacing:.3px;}
.sim-random-btn:hover{background:rgba(179,136,255,.2);}
.sim-bonus-sep{margin:18px 0 12px;border:none;border-top:1px solid var(--border);}
.sim-bonus-hdr{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--gold2);margin-bottom:10px;}
.sim-bonus-card{background:var(--bg-card);border:1px solid rgba(255,215,0,.12);border-radius:8px;padding:10px 12px;margin-bottom:7px;}
.sim-bonus-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:7px;}
.sim-bonus-lbl{font-size:.77rem;font-weight:600;}
.sim-bonus-val{font-size:.67rem;font-weight:700;color:var(--gold);}
.sim-bonus-sel{width:100%;background:var(--bg-card2);border:1px solid var(--border);color:var(--text);border-radius:6px;padding:6px 8px;font-size:.8rem;outline:none;cursor:pointer;transition:border-color .15s;}
.sim-bonus-sel:focus{border-color:rgba(255,215,0,.5);}
.sim-bonus-sel.selected{border-color:var(--gold);color:var(--gold);}
.mass-sim-area{border-top:2px solid var(--border);padding:24px 40px 40px;flex-shrink:0;}
.mass-sim-trigger{display:flex;align-items:center;gap:14px;margin-bottom:20px;flex-wrap:wrap;}
.mass-sim-title-row{font-size:1rem;font-weight:700;color:var(--text);display:flex;align-items:center;gap:10px;margin-bottom:16px;}
.mass-sim-btn{background:rgba(255,215,0,.08);border:1px solid rgba(255,215,0,.3);color:var(--gold);border-radius:8px;padding:9px 20px;font-size:.84rem;font-weight:600;cursor:pointer;letter-spacing:.3px;transition:all .2s;}
.mass-sim-btn:hover:not(:disabled){background:rgba(255,215,0,.15);}
.mass-sim-btn:disabled{opacity:.55;cursor:wait;}
.mass-sim-prog{font-size:.85rem;font-weight:700;color:var(--gold);min-width:40px;}
.mass-sim-note{font-size:.7rem;color:var(--muted);}
.mass-sim-scroll{overflow-x:auto;width:100%;border-radius:8px;border:1px solid var(--border);}
.mass-sim-tbl{border-collapse:collapse;width:100%;font-size:.71rem;}
.mass-sim-tbl th{padding:7px 6px;text-align:center;color:var(--muted);font-weight:600;font-size:.64rem;border-bottom:2px solid var(--border);white-space:nowrap;background:var(--bg-card2);position:sticky;top:0;}
.mass-sim-tbl td{padding:5px 6px;text-align:center;border:1px solid rgba(48,54,61,.25);font-variant-numeric:tabular-nums;}
.mass-sim-pos{font-weight:700;color:var(--text);background:var(--bg-card2)!important;font-size:.75rem;position:sticky;left:0;}
.mass-sim-pos.p1{color:var(--gold);}
.mass-sim-pos.p2{color:var(--silver);}
.mass-sim-pos.p3{color:var(--bronze);}
.mass-sim-sub{font-size:.7rem;color:var(--muted);margin-bottom:14px;}
/* Calculadora Final */
.calc-match-block{padding:14px 0 10px;border-bottom:1px solid var(--border);}
.calc-match-block:last-child{border-bottom:none;}
.calc-match-title{font-size:.78rem;font-weight:700;color:var(--gold);letter-spacing:.3px;margin-bottom:10px;}
.calc-section-lbl{font-size:.6rem;font-weight:700;color:var(--muted);letter-spacing:.8px;text-transform:uppercase;margin:8px 0 5px;}
.calc-res-row{display:flex;align-items:center;gap:6px;margin-bottom:6px;flex-wrap:wrap;}
.calc-team{font-size:.72rem;color:var(--text);font-weight:500;min-width:52px;}
.calc-sep{color:var(--muted);font-size:.85rem;flex-shrink:0;}
.calc-score-inp{width:38px;background:var(--bg-card2);border:1px solid var(--border);border-radius:5px;color:var(--text);padding:4px 5px;font-size:.8rem;text-align:center;-moz-appearance:textfield;outline:none;}
.calc-score-inp::-webkit-inner-spin-button,.calc-score-inp::-webkit-outer-spin-button{-webkit-appearance:none;}
.calc-score-inp:focus{border-color:rgba(255,215,0,.5);}
.calc-cls-sel{background:var(--bg-card2);border:1px solid var(--border);border-radius:5px;color:var(--text);padding:3px 5px;font-size:.7rem;outline:none;}
.calc-pred-grid{display:flex;flex-direction:column;gap:3px;}
.calc-pred-row{display:flex;align-items:center;gap:4px;}
.calc-pred-name{width:54px;font-size:.7rem;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex-shrink:0;}
.calc-p-inp{width:32px;}
.calc-cls-sm{font-size:.62rem;padding:2px 3px;}
.calc-bonus-block{padding:14px 0 6px;}
.calc-bonus-btns{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:4px;}
.calc-bon-btn{background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:6px;color:var(--muted);padding:4px 10px;font-size:.71rem;cursor:pointer;transition:all .15s;}
.calc-bon-btn.active{background:rgba(255,215,0,.1);border-color:var(--gold);color:var(--gold);font-weight:600;}
.calc-bon-btn:hover:not(.active){border-color:rgba(255,215,0,.35);color:var(--text);}
.calc-pos-num{color:var(--green);}
.calc-total-winner{color:var(--gold);}
.sim-rank-first{background:rgba(255,215,0,.04);border-radius:4px;}
/* Mobile bottom nav */
.mobile-bnav{display:none;position:fixed;bottom:0;left:0;right:0;background:var(--bg-card);border-top:1px solid var(--border);z-index:200;height:58px;}
.mob-btn{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6px 2px;color:var(--muted);font-size:.56rem;border:none;background:none;cursor:pointer;gap:3px;height:100%;}
.mob-btn .mi{font-size:1.1rem;}
.mob-btn.active{color:var(--gold);}
/* Hide rank columns on mobile */
.rk-hide-mob{}
@media(max-width:800px){body{display:block;height:auto;overflow:auto;}.sidebar{display:none;}.main-content,.sim-content,.relator-content,.tool-content{margin-left:0;height:auto;}.sim-body{flex-direction:column;}.sim-left{width:100%;border-right:none;border-bottom:1px solid var(--border);}.content-section{padding:20px 14px 28px;}.relator-body,.tool-body{padding:20px 14px 62px;}.tool-header{padding:20px 14px 16px;}.mobile-bnav{display:flex;overflow-x:auto;scrollbar-width:none;gap:0;}.mobile-bnav::-webkit-scrollbar{display:none;}.mob-btn{min-width:54px;flex:0 0 auto;}.main-content,.sim-content,.relator-content,.tool-content{padding-bottom:62px;}.s-dots{display:none;}.rk-hide-mob{display:none;}.chart-outer{height:300px;padding:12px;}.chart-mobile-legend{display:flex;flex-wrap:wrap;gap:6px 12px;padding:12px 4px 0;}.cml-item{display:flex;align-items:center;gap:5px;font-size:.72rem;color:var(--muted);}.cml-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}.rk-table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:thin;scrollbar-color:var(--border) transparent;}.rk-table-wrap::-webkit-scrollbar{height:4px;}.rk-table-wrap::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px;}.rank-table{font-size:.75rem;min-width:520px;}.rank-table th,.rank-table td{padding:8px 8px;}.rk-pts{font-size:.88rem;}.rk-form{gap:2px;}.rk-form-dot{width:6px;height:6px;}.badges-grid{grid-template-columns:1fr 1fr;gap:10px;}.badge-card{padding:14px;}.dif-bar-cell{min-width:120px;}.phase-name{width:120px;}.bonus-name{width:120px;}.day-match-name{min-width:120px;}}
</style>
</head>
<body>

<div id="loading"><div class="spinner"></div>Cargando datos...</div>

<div id="app" style="display:none">
  <aside class="sidebar">
    <div class="sidebar-brand">
      <div class="brand-label">Prode &middot; 2026</div>
      <div class="brand-title">Toros</div>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section">Panel principal</div>
      <button class="nav-item active" data-target="section-chart">
        <span class="nav-icon">&#128200;</span>Evolucion de Puntos
      </button>
      <button class="nav-item" data-target="section-ranking">
        <span class="nav-icon">&#127942;</span>Tabla de Posiciones
      </button>
      <button class="nav-item" data-target="section-bracket">
        <span class="nav-icon">&#9917;</span>Cuadro Eliminatorio
      </button>
      <button class="nav-item" data-target="section-fases">
        <span class="nav-icon">&#128197;</span>Por Fase
      </button>
      <button class="nav-item" data-target="section-bonus">
        <span class="nav-icon">&#11088;</span>Bonus
      </button>
      <div class="nav-divider"></div>
      <div class="nav-section">Herramientas</div>
      <button class="nav-item calc-nav" data-panel="sim">
        <span class="nav-icon">&#127942;</span>Calculadora Final
      </button>
      <button class="nav-item relator-nav" data-panel="relator">
        <span class="nav-icon">&#127908;</span>Relator de Prode
      </button>
      <div class="nav-divider"></div>
      <div class="nav-section">Estadisticas</div>
      <button class="nav-item" data-panel="badges">
        <span class="nav-icon">&#127941;</span>Premios
      </button>
      <button class="nav-item" data-panel="matrix">
        <span class="nav-icon">&#128202;</span>Predicciones
      </button>
      <button class="nav-item" data-panel="dificultad">
        <span class="nav-icon">&#127919;</span>Dificultad
      </button>
    </nav>
    <div class="sidebar-footer">
      <div class="footer-updated" id="footer-updated"></div>
      <div class="finale-banner">
        <div class="finale-banner-title">&#127942; Gran Final</div>
        <div class="finale-banner-sub">Argentina v Espa&ntilde;a &middot; $400.000</div>
      </div>
      <div class="leader-card" id="leader-card"></div>
    </div>
  </aside>

  <main class="main-content" id="main-content">

    <section id="section-chart" class="content-section">
      <div class="section-header">
        <div>
          <div class="section-title"><div class="section-bar"></div>Evolucion de Puntos</div>
          <div class="section-desc">Hover sobre una linea para resaltarla &nbsp;&middot;&nbsp; Scroll para zoom &nbsp;&middot;&nbsp; Drag para mover</div>
        </div>
        <button class="reset-zoom-btn" id="reset-zoom-btn">&#8635; Reset zoom</button>
      </div>
      <div class="chart-outer">
        <canvas id="evolutionChart"></canvas>
      </div>
      <div class="chart-mobile-legend" id="chart-mobile-legend"></div>
    </section>

    <section id="section-ranking" class="content-section">
      <div class="section-header">
        <div>
          <div class="section-title"><div class="section-bar"></div>Tabla de Posiciones</div>
          <div class="section-desc" id="ranking-desc"></div>
        </div>
      </div>
      <div class="legend-row">
        <div class="legend-item"><div class="legend-dot" style="background:var(--green)"></div>Comun (2 pts grupos)</div>
        <div class="legend-item"><div class="legend-dot" style="background:var(--gold)"></div>Exacto (5 pts grupos)</div>
        <div class="legend-item"><div class="legend-dot" style="background:var(--gold2)"></div>Exacto + Bonus (7 pts grupos)</div>
      </div>
      <div class="rk-table-wrap">
      <table class="rank-table">
        <thead>
          <tr>
            <th style="text-align:center">#</th>
            <th style="text-align:left">Jugador</th>
            <th>Pts</th>
            <th title="Simulacion Monte Carlo 6000 iteraciones. Asume rendimiento historico + clasificados 50/50.">% Win</th>
            <th>Prom.</th>
            <th title="Resultados exactos en grupos (5 pts)">Exactos</th>
            <th title="Exactos con bonus en grupos (7 pts)">Ex+B</th>
            <th>Ult. 5</th>
            <th>Forma</th>
          </tr>
        </thead>
        <tbody id="rank-tbody"></tbody>
      </table>
      </div>
    </section>

    <section id="section-bracket" class="content-section">
      <div class="section-header">
        <div>
          <div class="section-title"><div class="section-bar"></div>Cuadro Eliminatorio</div>
          <div class="section-desc">Click en un partido para ver las predicciones &nbsp;&middot;&nbsp; Partidos sin datos aparecen atenuados</div>
        </div>
      </div>
      <div class="bracket-wrap">
        <div class="bracket" id="bracket">
          <svg id="bracket-svg"></svg>
        </div>
      </div>
      <div class="pred-detail" id="pred-detail"></div>
    </section>

    <section id="section-fases" class="content-section">
      <div class="section-header">
        <div>
          <div class="section-title"><div class="section-bar" style="background:var(--gold)"></div>Rendimiento por Fase</div>
          <div class="section-desc">Puntos acumulados en cada etapa del torneo &nbsp;&middot;&nbsp; Click en la fase para ver el detalle</div>
        </div>
      </div>
      <div class="phase-tabs" id="phase-tabs"></div>
      <div id="phase-contents"></div>
    </section>

    <section id="section-bonus" class="content-section">
      <div class="section-header">
        <div>
          <div class="section-title"><div class="section-bar" style="background:var(--gold2)"></div>Bonus Pre-Torneo</div>
          <div class="section-desc">Predicciones selladas antes del torneo &nbsp;&middot;&nbsp; Campeon, Subcampeon, Goleador y mas &nbsp;&middot;&nbsp; 60 pts en juego</div>
        </div>
      </div>
      <div id="bonus-body"></div>
    </section>

  </main>

  <div class="sim-content" id="sim-content" style="display:none">
    <div class="sim-header">
      <div class="sim-title-block">
        <div class="sim-title"><div class="section-bar"></div>Calculadora Final</div>
        <div class="sim-subtitle">Ingresa predicciones y resultado hipotetico &nbsp;&middot;&nbsp; Solo jugadores con chance matematica (max &gt; 270 pts)</div>
        <div style="margin-top:8px;font-size:.72rem;color:var(--gold2);background:rgba(255,215,0,.06);border:1px solid rgba(255,215,0,.18);border-radius:6px;padding:7px 12px;display:inline-block;">&#127942; P103 y P104 pendientes de predicciones &nbsp;&middot;&nbsp; Bonus: Campeon, Goleador, Mas goles activos &nbsp;&middot;&nbsp; Max posible Tomi: 270 pts</div>
      </div>
    </div>
    <div class="sim-body">
      <div class="sim-left" id="calc-left-panel" style="width:430px;max-width:430px"></div>
      <div class="sim-right">
        <div class="sim-right-header">Contendientes al titulo &#127942;</div>
        <div id="calc-rank-list"></div>
      </div>
    </div>
  </div>

  <div class="relator-content" id="relator-content" style="display:none">
    <div class="relator-header">
      <div>
        <div class="relator-title"><div class="section-bar" style="background:var(--pink)"></div>Relator de Prode</div>
        <div class="relator-subtitle">La cronica del Prode Toros, en vivo y en directo</div>
      </div>
      <button class="relator-btn" id="relator-btn">&#127908; Relatar de nuevo</button>
    </div>
    <div class="relator-body" id="relator-body"></div>
  </div>

  <div class="tool-content" id="badges-content" style="display:none">
    <div class="tool-header">
      <div class="tool-title"><div class="section-bar" style="background:var(--gold)"></div>Premios</div>
      <div class="tool-subtitle">Fase de grupos y eliminatorio — estadisticas calculadas automaticamente</div>
    </div>
    <div class="tool-body" id="badges-body"></div>
  </div>

  <div class="tool-content" id="matrix-content" style="display:none">
    <div class="tool-header">
      <div class="tool-title"><div class="section-bar" style="background:var(--gold)"></div>Matriz de Predicciones</div>
      <div class="tool-subtitle">Que predijo cada uno en cada partido jugado — verde=exacto, amarillo=comun, rojo=fallo</div>
    </div>
    <div class="tool-body" id="matrix-body"></div>
  </div>

  <div class="tool-content" id="dificultad-content" style="display:none">
    <div class="tool-header">
      <div class="tool-title"><div class="section-bar" style="background:var(--pink)"></div>Partidos por Dificultad</div>
      <div class="tool-subtitle">Los 72 partidos de grupos ordenados por cuantos jugadores acertaron la direccion</div>
    </div>
    <div class="tool-body" id="dificultad-body"></div>
  </div>

  <div class="s-dots" id="s-dots">
    <button class="s-dot active" title="Evolucion"></button>
    <button class="s-dot" title="Tabla"></button>
    <button class="s-dot" title="Bracket"></button>
    <button class="s-dot" title="Por Fase"></button>
    <button class="s-dot" title="Bonus"></button>
  </div>

  <nav class="mobile-bnav">
    <button class="mob-btn active" data-target="section-chart"><span class="mi">&#128200;</span>Evol.</button>
    <button class="mob-btn" data-target="section-ranking"><span class="mi">&#127942;</span>Tabla</button>
    <button class="mob-btn" data-target="section-bracket"><span class="mi">&#9917;</span>Bracket</button>
    <button class="mob-btn" data-target="section-fases"><span class="mi">&#128197;</span>Fases</button>
    <button class="mob-btn" data-target="section-bonus"><span class="mi">&#11088;</span>Bonus</button>
    <button class="mob-btn" data-panel="sim"><span class="mi">&#127942;</span>Final</button>
    <button class="mob-btn" data-panel="relator"><span class="mi">&#127908;</span>Relator</button>
    <button class="mob-btn" data-panel="badges"><span class="mi">&#127941;</span>Premios</button>
    <button class="mob-btn" data-panel="matrix"><span class="mi">&#128202;</span>Preds.</button>
    <button class="mob-btn" data-panel="dificultad"><span class="mi">&#127919;</span>Dific.</button>
  </nav>

</div>

<script>
var _reAcc = new RegExp('[\\u0300-\\u036f]', 'g');
function abbrevTeam(t){var s=t.trim().normalize('NFD').replace(_reAcc,'').replace(/^(RI de |Rep\. de |Rep\. |RD |Estados |Arabia |Nueva )/i,'');return s.substring(0,3).toUpperCase();}
function abbrevMatch(name){var p=name.split(' vs ');if(p.length<2)p=name.split(' v ');return p.length===2?abbrevTeam(p[0])+'-'+abbrevTeam(p[1]):name.substring(0,7);}
function resultType(score){var p=score.split('-').map(Number);if(isNaN(p[0])||isNaN(p[1]))return'tie';return p[0]>p[1]?'local':p[0]<p[1]?'away':'tie';}
function formDotClass(pts){if(!pts)return'miss';if(pts>=7)return'bonus';if(pts>=5)return'exact';return'common';}
function _pick(arr){return arr[Math.floor(Math.random()*arr.length)];}

var _winProbs=null;
function calcWinProbs(data){
  var N=6000,players=data.players,base={};
  data.ranking.forEach(function(r){base[r.name]=r.pts;});

  // Distribucion historica individual
  var dists={};
  players.forEach(function(p){
    var h=data.history[p]||[0],d=[];
    for(var i=1;i<h.length;i++)d.push(h[i]-h[i-1]);
    var tot=d.length||1,nm=0,nc=0,ne=0,nb=0;
    d.forEach(function(v){if(!v)nm++;else if(v<5)nc++;else if(v<9)ne++;else nb++;});
    dists[p]={m:nm/tot,c:nc/tot,e:ne/tot,b:nb/tot};
  });

  // Promedio global (regresion a la media):
  // 72 partidos de grupos es buena muestra pero el knockout es distinto.
  // Blend 50% individual / 50% global reduce la ventaja de los lideres
  // sin ignorar la habilidad real — es un estimador mas honesto.
  var gm=0,gc=0,ge=0,gb=0,np=players.length;
  players.forEach(function(p){gm+=dists[p].m;gc+=dists[p].c;ge+=dists[p].e;gb+=dists[p].b;});
  gm/=np;gc/=np;ge/=np;gb/=np;
  var alpha=0.5;
  players.forEach(function(p){
    dists[p]={
      m:alpha*dists[p].m+(1-alpha)*gm,
      c:alpha*dists[p].c+(1-alpha)*gc,
      e:alpha*dists[p].e+(1-alpha)*ge,
      b:alpha*dists[p].b+(1-alpha)*gb
    };
  });

  var rem=(data.knockout_matches||[]).filter(function(m){return!m.played;});
  // Puntos reales por fase (exacto / comun)
  var phE={'16avos':5,'Octavos':7,'Cuartos':7,'Semis':7,'3er Puesto':7,'Final':10};
  var phC={'16avos':2,'Octavos':3,'Cuartos':3,'Semis':3,'3er Puesto':3,'Final':5};

  if(!rem.length){
    var mxB=Math.max.apply(null,players.map(function(p){return base[p]||0;}));
    var pb={};players.forEach(function(p){pb[p]=(base[p]||0)===mxB?1:0;});return pb;
  }
  var wins={};players.forEach(function(p){wins[p]=0;});
  for(var s=0;s<N;s++){
    var sp={};players.forEach(function(p){sp[p]=base[p]||0;});
    rem.forEach(function(m){
      var ex=phE[m.phase]||5,cm=phC[m.phase]||2;
      // Simular resultado del partido (igual para todos en esta iteracion)
      // Esto captura la correlacion real: si el resultado es X, todos
      // que predijeron X suman; los que no, no.
      var matchR=Math.random();
      players.forEach(function(p){
        var ds=dists[p],r=Math.random(),pts=0;
        if(r<ds.m)pts=0;
        else if(r<ds.m+ds.c)pts=cm;
        else if(r<ds.m+ds.c+ds.e)pts=ex;
        else pts=ex+2;
        if(matchR<0.5)pts+=2; // clasificado: mismo resultado para todos
        sp[p]+=pts;
      });
    });
    var mxP=players.reduce(function(a,p){return sp[p]>sp[a]?p:a;},players[0]);
    var mxV=sp[mxP],tie=players.filter(function(p){return sp[p]===mxV;});
    tie.forEach(function(p){wins[p]+=1/tie.length;});
  }
  var probs={};players.forEach(function(p){probs[p]=wins[p]/N;});
  return probs;
}

function renderRanking(data){
  _winProbs=calcWinProbs(data);
  var pc3=['p1','p2','p3'];
  document.getElementById('rank-tbody').innerHTML=data.ranking.map(function(r,i){
    var pc=i<3?pc3[i]:'',c=data.colors[r.name]||'#888';
    var hist=data.history[r.name]||[0],deltas=[];
    for(var d=1;d<hist.length;d++)deltas.push(hist[d]-hist[d-1]);
    var avg=deltas.length>0?(r.pts/deltas.length).toFixed(1):'0';
    var exactos=deltas.filter(function(d){return d>=5;}).length;
    var exactosB=deltas.filter(function(d){return d===7;}).length;
    var last5=deltas.slice(-5).reduce(function(a,b){return a+b;},0);
    var dots=deltas.slice(-5).map(function(v){return'<div class="rk-form-dot '+formDotClass(v)+'" title="'+v+' pts"></div>';}).join('');
    var prob=_winProbs?_winProbs[r.name]:null;
    var probStr=prob===null?'—':prob<0.005?'<1%':(prob*100).toFixed(1)+'%';
    var probCls='rk-win'+(prob>0.45?' rk-win-hi':prob>0.15?' rk-win-mid':prob<0.04?' rk-win-lo':'');
    return'<tr><td class="rk-pos '+pc+'">'+r.pos+'</td><td><div class="rk-name"><span class="clr-dot" style="background:'+c+'"></span>'+r.name+'</div></td><td class="rk-pts '+pc+'">'+r.pts+'</td><td class="'+probCls+'">'+probStr+'</td><td class="rk-stat rk-hide-mob">'+avg+'</td><td class="rk-stat rk-hide-mob'+(exactos>0?' gold':'')+'">'+exactos+'</td><td class="rk-stat rk-hide-mob'+(exactosB>0?' gold2':'')+'">'+exactosB+'</td><td class="rk-stat">'+last5+'</td><td><div class="rk-form">'+dots+'</div></td></tr>';
  }).join('');
  document.getElementById('ranking-desc').textContent=data.matches_played.length+' partidos de grupos jugados';
}

var hoveredDsIdx=-1,chartInstance=null;
var dimPlugin={id:'dim',beforeDatasetDraw:function(chart,args){if(hoveredDsIdx===-1)return;chart.ctx.globalAlpha=args.index===hoveredDsIdx?1:0.07;},afterDatasetDraw:function(chart){chart.ctx.globalAlpha=1;}};
function renderChart(data){
  if(chartInstance){chartInstance.destroy();hoveredDsIdx=-1;}
  var isMob=window.innerWidth<800;
  var labels=['Inicio'].concat(data.matches_played.map(abbrevMatch));
  var datasets=data.players.map(function(name){return{label:name,data:data.history[name],borderColor:data.colors[name]||'#fff',backgroundColor:data.colors[name]||'#fff',tension:0.2,borderWidth:isMob?2:1.5,pointRadius:0,pointHoverRadius:4};});
  var drawNamesPlugin={id:'drawNames',afterDraw:function(chart){var ctx=chart.ctx,right=chart.chartArea.right,yS=chart.scales.y;ctx.save();ctx.font='bold 12px sans-serif';ctx.textBaseline='middle';var groups={};chart.data.datasets.forEach(function(ds,di){var v=ds.data[ds.data.length-1];if(!groups[v])groups[v]=[];groups[v].push({name:ds.label,color:ds.borderColor,di:di});});var MIN=18;var pos=Object.keys(groups).sort(function(a,b){return b-a;}).map(function(s){return{score:s,ty:yS.getPixelForValue(+s),ay:yS.getPixelForValue(+s),items:groups[s]};});var prev=-999;pos.forEach(function(p){if(p.ty<prev+MIN)p.ay=prev+MIN;prev=p.ay;});pos.forEach(function(pos2){var x=right+14;if(Math.abs(pos2.ty-pos2.ay)>2){ctx.globalAlpha=.3;ctx.beginPath();ctx.moveTo(right,pos2.ty);ctx.lineTo(right+9,pos2.ay);ctx.strokeStyle='#7d8590';ctx.lineWidth=1;ctx.stroke();ctx.globalAlpha=1;}pos2.items.forEach(function(item,idx){var active=hoveredDsIdx===-1||hoveredDsIdx===item.di;ctx.globalAlpha=active?1:0.08;ctx.fillStyle=item.color;ctx.fillText(item.name,x,pos2.ay);x+=ctx.measureText(item.name).width;if(idx<pos2.items.length-1){ctx.fillStyle='#7d8590';ctx.fillText(' / ',x,pos2.ay);x+=ctx.measureText(' / ').width;}else{ctx.fillStyle=active?'#aabbcc':'#222';ctx.fillText(' ('+pos2.score+')',x,pos2.ay);}ctx.globalAlpha=1;});});ctx.restore();}};
  var ctx2d=document.getElementById('evolutionChart').getContext('2d');
  chartInstance=new Chart(ctx2d,{type:'line',data:{labels:labels,datasets:datasets},options:{responsive:true,maintainAspectRatio:false,layout:{padding:{right:isMob?4:340}},interaction:{mode:'index',intersect:false},scales:{y:{beginAtZero:true,grid:{color:'rgba(255,255,255,.07)'},ticks:{color:'#7d8590',font:{size:isMob?10:12}}},x:{grid:{display:false},ticks:{color:'#7d8590',maxRotation:90,minRotation:90,font:{size:9},autoSkip:isMob,maxTicksLimit:isMob?15:999}}},plugins:{legend:{display:false},tooltip:{mode:'index',intersect:false,itemSort:function(a,b){return b.raw-a.raw;},backgroundColor:'rgba(13,17,23,.97)',titleColor:'#00e5ff',bodyColor:'#ccc',borderColor:'#30363d',borderWidth:1,padding:10,callbacks:{label:function(){return null;},beforeBody:function(items){return items.map(function(it,i){return'  '+(i+1)+'. '+it.dataset.label+': '+it.raw;});}}},zoom:{pan:{enabled:true,mode:'x'},zoom:{wheel:{enabled:true,speed:0.08},pinch:{enabled:true},mode:'x'}}}},plugins:isMob?[]:[ dimPlugin,drawNamesPlugin]});
  // Leyenda mobile: grid compacto de colores + nombres debajo del chart
  var legEl=document.getElementById('chart-mobile-legend');
  if(legEl){legEl.innerHTML=data.players.map(function(p){return'<span class="cml-item"><span class="cml-dot" style="background:'+(data.colors[p]||'#ccc')+'"></span>'+p.split(' ')[0]+'</span>';}).join('');}
  document.getElementById('reset-zoom-btn').onclick=function(){if(chartInstance)chartInstance.resetZoom();};
  var canvas=document.getElementById('evolutionChart');
  canvas.addEventListener('mousemove',function(evt){var ca=chartInstance.chartArea,mx=evt.offsetX,my=evt.offsetY;if(mx<ca.left||mx>ca.right||my<ca.top||my>ca.bottom){if(hoveredDsIdx!==-1){hoveredDsIdx=-1;chartInstance.update('none');}return;}var xVal=chartInstance.scales.x.getValueForPixel(mx);var di=Math.max(0,Math.min(Math.round(xVal),chartInstance.data.labels.length-1));var minD=18,near=-1;chartInstance.data.datasets.forEach(function(ds,i){var v=ds.data[di];if(v===undefined||v===null)return;var d=Math.abs(my-chartInstance.scales.y.getPixelForValue(v));if(d<minD){minD=d;near=i;}});if(near!==hoveredDsIdx){hoveredDsIdx=near;chartInstance.update('none');}});
  canvas.addEventListener('mouseleave',function(){if(hoveredDsIdx!==-1){hoveredDsIdx=-1;chartInstance.update('none');}});
}

var _koData=null;
var PHASE_META={'16avos':{label:'16AVOS',color:'#00e5ff'},'Octavos':{label:'OCTAVOS',color:'#ff8c00'},'Cuartos':{label:'CUARTOS',color:'#69ff47'},'Semis':{label:'SEMIFINAL',color:'#ff4081'},'Final':{label:'FINAL',color:'#ffd700'},'3er Puesto':{label:'3ER PUESTO',color:'#b388ff'}};
function posRelTo(el,c){var t=0,l=0,cur=el;while(cur&&cur!==c){t+=cur.offsetTop;l+=cur.offsetLeft;cur=cur.offsetParent;}return{top:t,left:l,w:el.offsetWidth,h:el.offsetHeight};}
function svgLine(svg,x1,y1,x2,y2){var l=document.createElementNS('http://www.w3.org/2000/svg','line');l.setAttribute('x1',x1);l.setAttribute('y1',y1);l.setAttribute('x2',x2);l.setAttribute('y2',y2);l.setAttribute('stroke','#2d333b');l.setAttribute('stroke-width','1.5');svg.appendChild(l);}
function drawBracketLines(){var br=document.getElementById('bracket'),svg=document.getElementById('bracket-svg');svg.innerHTML='';svg.setAttribute('width',br.scrollWidth);svg.setAttribute('height',br.scrollHeight);var cols=Array.from(br.querySelectorAll('.br-col')).filter(function(c){return c.dataset.phase!=='3er Puesto';});for(var ci=0;ci<cols.length-1;ci++){var cur=Array.from(cols[ci].querySelectorAll('.bm')),nxt=Array.from(cols[ci+1].querySelectorAll('.bm'));if(!cur.length||!nxt.length)continue;var ratio=Math.round(cur.length/nxt.length);for(var ni=0;ni<nxt.length;ni++){var s=ni*ratio,e=Math.min(s+ratio,cur.length);if(e<=s)continue;var nc=posRelTo(nxt[ni],br),c1=posRelTo(cur[s],br),c2=posRelTo(cur[e-1],br);var x1=c1.left+c1.w,y1=c1.top+c1.h/2,x2=c2.left+c2.w,y2=c2.top+c2.h/2,x3=nc.left,y3=nc.top+nc.h/2,xm=x1+(x3-x1)*0.5;svgLine(svg,x1,y1,xm,y1);svgLine(svg,x2,y2,xm,y2);svgLine(svg,xm,y1,xm,y2);svgLine(svg,xm,y3,x3,y3);}}}
function showPredDetail(match){var detail=document.getElementById('pred-detail');var groups={};if(_koData&&_koData.players){_koData.players.forEach(function(p){var pr=match.predictions[p];if(!pr)return;if(!groups[pr])groups[pr]=[];groups[pr].push(p);});}var sorted=Object.keys(groups).map(function(s){return{score:s,voters:groups[s]};}).sort(function(a,b){return b.voters.length-a.voters.length;});var local=0,tie=0,away=0;sorted.forEach(function(g){var t=resultType(g.score);if(t==='local')local+=g.voters.length;else if(t==='away')away+=g.voters.length;else tie+=g.voters.length;});var teams=match.match.split(' vs ');var total=local+tie+away;var pg=sorted.map(function(g){var t=resultType(g.score);var names=g.voters.map(function(v){var cls=match.classif&&match.classif[v]?'<span class="pg-classif">→ '+match.classif[v]+'</span>':'';return v+cls;}).join('<br>');return'<div class="pg"><div class="pg-score '+t+'">'+g.score+'</div><div class="pg-count">'+g.voters.length+' voto'+(g.voters.length!==1?'s':'')+'</div><div class="pg-names">'+names+'</div></div>';}).join('');var rbar='';if(local>0)rbar+='<span class="psum"><span class="psum-dot" style="background:var(--cyan)"></span>'+(teams[0]||'Local')+': '+local+'</span>';if(tie>0)rbar+='<span class="psum"><span class="psum-dot" style="background:var(--violet)"></span>Empate: '+tie+'</span>';if(away>0)rbar+='<span class="psum"><span class="psum-dot" style="background:var(--pink)"></span>'+(teams[1]||'Visitante')+': '+away+'</span>';detail.innerHTML='<div class="pred-head"><div><div class="pred-match-name">'+match.match+'</div><div class="pred-match-meta">'+match.phase+' &nbsp;&middot;&nbsp; '+match.id+' &nbsp;&middot;&nbsp; '+total+' predicciones</div></div><button class="pred-close" onclick="closePredDetail()">&#10005; Cerrar</button></div>'+(rbar?'<div class="pred-summary">'+rbar+'</div>':'')+'<div class="pred-groups">'+pg+'</div>';detail.classList.add('open');setTimeout(function(){detail.scrollIntoView({behavior:'smooth',block:'nearest'});},60);}
function closePredDetail(){document.getElementById('pred-detail').classList.remove('open');document.querySelectorAll('.bm').forEach(function(c){c.classList.remove('selected');});}
function renderBracket(data){_koData=data;var ko=data.knockout_matches;var br=document.getElementById('bracket'),svg=document.getElementById('bracket-svg');var phOrd=['16avos','Octavos','Cuartos','Semis','Final','3er Puesto'],phMap={};ko.forEach(function(m){if(!phMap[m.phase])phMap[m.phase]=[];phMap[m.phase].push(m);});var html='';phOrd.forEach(function(phase){var ms=phMap[phase];if(!ms||!ms.length)return;var meta=PHASE_META[phase]||{label:phase.toUpperCase(),color:'#00e5ff'};var slots=ms.map(function(m){var cls='bm';if(m.is_tbd)cls+=' tbd';else if(!m.show_preds)cls+=' locked';else if(m.has_preds)cls+=' clickable';if(m.played)cls+=' played';if(phase==='Final')cls+=' bm-final';if(phase==='3er Puesto')cls+=' bm-3rd';var mnCls=m.is_tbd?'bm-match tbd-name':'bm-match';var dots='';if(!m.is_tbd&&m.show_preds&&data.players){var cnt=data.players.filter(function(p){return!!m.predictions[p];}).length;dots='<div class="bm-dots">';for(var d=0;d<Math.min(cnt,8);d++)dots+='<div class="bd on'+(m.played?' played':'')+'"></div>';for(var d2=cnt;d2<8;d2++)dots+='<div class="bd"></div>';dots+='</div>';}else if(!m.is_tbd&&!m.show_preds){dots='<div class="bm-lock">&#128274;'+(m.match_date?' '+m.match_date:'')+'</div>';}return'<div class="'+cls+'" data-id="'+m.id+'"><div class="bm-id">'+m.id+'</div><div class="'+mnCls+'">'+m.match+'</div>'+dots+'</div>';}).join('');html+='<div class="br-col" data-phase="'+phase+'"><div class="br-col-header" style="color:'+meta.color+'">'+meta.label+'</div><div class="br-slots">'+slots+'</div></div>';});br.innerHTML=html;br.appendChild(svg);br.querySelectorAll('.bm.clickable').forEach(function(card){card.addEventListener('click',function(){var mid=this.dataset.id;var match=ko.find(function(m){return m.id===mid;});if(!match)return;var was=this.classList.contains('selected');br.querySelectorAll('.bm').forEach(function(c){c.classList.remove('selected');});if(was){closePredDetail();return;}this.classList.add('selected');showPredDetail(match);});});requestAnimationFrame(function(){requestAnimationFrame(drawBracketLines);});
// Mostrar resultado real en partidos jugados
ko.filter(function(m){return m.played;}).forEach(function(m){
  var card=br.querySelector('.bm[data-id="'+m.id+'"]');if(!card)return;
  var players=data.players;var maxPts=0;
  players.forEach(function(p){if((m.points[p]||0)>maxPts)maxPts=m.points[p]||0;});
  if(maxPts===0)return;
  var topPlayer=players.find(function(p){return(m.points[p]||0)===maxPts;});
  if(!topPlayer||!m.predictions[topPlayer])return;
  var parts=m.predictions[topPlayer].split('-');if(parts.length<2)return;
  var scoreStr=parts[0]+' - '+parts[1];
  var clsTeam='';
  if(m.classif){
    var teams=m.match.split(' v ');
    var lT=(teams[0]||'').trim().toLowerCase().slice(0,4);
    var scorePtsOnly=_calcPts(m.predictions[topPlayer],{l:+parts[0],a:+parts[1]},m.phase);
    var clsPlayer=null;
    if((m.points[topPlayer]||0)>scorePtsOnly&&m.classif[topPlayer]){
      clsPlayer=topPlayer;
    } else {
      var inferScore={l:+parts[0],a:+parts[1]};
      clsPlayer=players.find(function(p){
        if(!m.classif[p])return false;
        var pPts=m.points[p]||0;
        var pSc=_calcPts(m.predictions[p],inferScore,m.phase);
        return pPts>0&&pPts===pSc+2;
      })||null;
    }
    if(clsPlayer){
      var cls=m.classif[clsPlayer].toLowerCase().slice(0,4);
      clsTeam=(cls===lT)?teams[0]:(teams[1]||'');
    }
  }
  var el=document.createElement('div');el.className='bm-result';
  el.textContent=scoreStr+(clsTeam?' • '+clsTeam.trim()+' pasa':'');
  var matchEl=card.querySelector('.bm-match');
  if(matchEl)matchEl.insertAdjacentElement('afterend',el);
});}

var _CHANCE_PLAYERS=['Tomi Marchiano','Nico Conti','JZ','Patru Maqui','Lucas Tkacz','Tomi Samitier','Nico Gianola','Fran Garoby','Alejo Di Fiori'];
var _CALC_PH={'3er Puesto':{common:3,exact:7,gol:3,cls:2},'Final':{common:5,exact:10,gol:5,cls:2}};
var _CALC_MATCHES=[{id:'P103',phase:'3er Puesto',label:'P103 — 3er Puesto: Francia v Inglaterra',teams:['Francia','Inglaterra']},{id:'P104',phase:'Final',label:'P104 — Gran Final ★: Argentina v España',teams:['Argentina','España']}];
var _calcData=null,_calcBonusPicks={},_calcBonus={};
function _normStr(s){return(s||'').trim().toLowerCase().replace(/á/g,'a').replace(/é/g,'e').replace(/í/g,'i').replace(/ó/g,'o').replace(/ú/g,'u').replace(/ñ/g,'n').replace(/Á/g,'a').replace(/É/g,'e').replace(/Í/g,'i').replace(/Ó/g,'o').replace(/Ú/g,'u').replace(/Ñ/g,'n');}
function _calcPid(p){return p.replace(/[^a-zA-Z]/g,'');}
function _calcMatchPts(ps,pr,isFinal){if(ps===null||pr===null||ps===''||pr==='')return 0;var p=isFinal?_CALC_PH['Final']:_CALC_PH['3er Puesto'];var pp=String(ps).split('-').map(Number),rp=String(pr).split('-').map(Number);if(pp.some(isNaN)||rp.some(isNaN))return 0;var pDir=pp[0]>pp[1]?1:pp[0]<pp[1]?-1:0,rDir=rp[0]>rp[1]?1:rp[0]<rp[1]?-1:0;if(pDir!==rDir)return 0;var pts=pp[0]===rp[0]&&pp[1]===rp[1]?p.exact:p.common;if(Math.abs(pp[0]-pp[1])>=3&&Math.abs(rp[0]-rp[1])>=3)pts+=p.gol;return pts;}
function _calcClsPts(predCls,realCls,isFinal){var p=isFinal?_CALC_PH['Final']:_CALC_PH['3er Puesto'];return(predCls&&realCls&&_normStr(predCls)===_normStr(realCls))?p.cls:0;}
function _calcBonusForPlayer(player){var picks=_calcBonusPicks[player]||{};var pts=0;var s1=_calcBonus['B1']||'';if(s1&&picks['B1']&&_normStr(picks['B1'])===_normStr(s1))pts+=12;if(s1){var sub=_normStr(s1)==='argentina'?'espana':'argentina';if(picks['B2']&&_normStr(picks['B2'])===sub)pts+=8;}var s3=_calcBonus['B3']||'';if(s3&&picks['B3']&&_normStr(picks['B3'])===_normStr(s3))pts+=8;var s4=_calcBonus['B4']||'';if(s4&&picks['B4']&&_normStr(picks['B4'])===_normStr(s4))pts+=5;return pts;}
function _calcUpdate(){if(!_calcData)return;function gv(id){var el=document.getElementById(id);return el?el.value:'';}function gi(id){var v=parseInt(gv(id));return isNaN(v)?null:v;}var p103={},p104={},pb={};_CHANCE_PLAYERS.forEach(function(player){var pid=_calcPid(player);var r1g1=gi('P103-r1'),r1g2=gi('P103-r2'),r1cls=gv('P103-rcls');var p1g1=gi('P103-p-'+pid+'-1'),p1g2=gi('P103-p-'+pid+'-2'),p1cls=gv('P103-p-'+pid+'-cls');var m103=0;if(r1g1!==null&&r1g2!==null&&p1g1!==null&&p1g2!==null)m103+=_calcMatchPts(p1g1+'-'+p1g2,r1g1+'-'+r1g2,false);m103+=_calcClsPts(p1cls,r1cls,false);p103[player]=m103;var r4g1=gi('P104-r1'),r4g2=gi('P104-r2'),r4cls=gv('P104-rcls');var p4g1=gi('P104-p-'+pid+'-1'),p4g2=gi('P104-p-'+pid+'-2'),p4cls=gv('P104-p-'+pid+'-cls');var m104=0;if(r4g1!==null&&r4g2!==null&&p4g1!==null&&p4g2!==null)m104+=_calcMatchPts(p4g1+'-'+p4g2,r4g1+'-'+r4g2,true);m104+=_calcClsPts(p4cls,r4cls,true);p104[player]=m104;pb[player]=_calcBonusForPlayer(player);});function basePts(p){var r=(_calcData.ranking||[]).find(function(r){return r.name===p;});return r?r.pts:0;}var sorted=_CHANCE_PLAYERS.slice().sort(function(a,b){return(basePts(b)+p103[b]+p104[b]+pb[b])-(basePts(a)+p103[a]+p104[a]+pb[a]);});var medals=['\u{1F3C5}','\u{1F948}','\u{1F949}'];var html='<div class="sim-rank-row" style="font-size:.58rem;font-weight:700;color:var(--muted);text-transform:uppercase;padding-bottom:6px;border-bottom:2px solid var(--border);margin-bottom:4px"><span></span><span>Jugador</span><span style="text-align:right">Base</span><span style="text-align:right">P103</span><span style="text-align:right">P104</span><span style="text-align:right">Bonus</span><span style="text-align:right">Total</span></div>';sorted.forEach(function(player,i){var base=basePts(player),p3=p103[player],p4=p104[player],pbo=pb[player],tot=base+p3+p4+pbo;var pos=i<3?medals[i]:(i+1)+'';var pc=i<3?['p1','p2','p3'][i]:'';var c=(_calcData.colors||{})[player]||'#888';html+='<div class="sim-rank-row'+(i===0?' sim-rank-first':'')+'"><div class="sim-rank-pos '+pc+'">'+pos+'</div><div class="sim-rank-name"><span class="clr-dot" style="background:'+c+'"></span>'+player.split(' ')[0]+'</div><div class="sim-rank-num">'+base+'</div><div class="sim-rank-num '+(p3>0?'calc-pos-num':'')+'">'+((p3>0)?'+'+p3:(p3<0?String(p3):'&#x2014;'))+'</div><div class="sim-rank-num '+(p4>0?'calc-pos-num':'')+'">'+((p4>0)?'+'+p4:(p4<0?String(p4):'&#x2014;'))+'</div><div class="sim-rank-num '+(pbo>0?'calc-pos-num':'')+'">'+((pbo>0)?'+'+pbo:'&#x2014;')+'</div><div class="sim-rank-total '+pc+(i===0?' calc-total-winner':'')+'" style="text-align:right">'+tot+'</div></div>';});document.getElementById('calc-rank-list').innerHTML=html;}
function _calcBonusPick(bid,val){_calcBonus[bid]=val||'';document.querySelectorAll('[data-cbid="'+bid+'"]').forEach(function(b){b.classList.toggle('active',b.dataset.cbval===(val||''));});_calcUpdate();}
function _buildCalcPanel(data){var panel=document.getElementById('calc-left-panel');if(!panel)return;var html='';_CALC_MATCHES.forEach(function(m){html+='<div class="calc-match-block"><div class="calc-match-title">'+m.label+'</div>';html+='<div class="calc-section-lbl">Resultado hipotético</div><div class="calc-res-row"><span class="calc-team">'+m.teams[0]+'</span><input type="number" class="calc-score-inp" id="'+m.id+'-r1" min="0" max="15" placeholder="0" oninput="_calcUpdate()"><span class="calc-sep"> − </span><input type="number" class="calc-score-inp" id="'+m.id+'-r2" min="0" max="15" placeholder="0" oninput="_calcUpdate()"><span class="calc-team">'+m.teams[1]+'</span><select class="calc-cls-sel" id="'+m.id+'-rcls" onchange="_calcUpdate()" style="margin-left:8px"><option value="">— Gan.</option>';m.teams.forEach(function(t){html+='<option value="'+t+'">'+t+'</option>';});html+='</select></div>';html+='<div class="calc-section-lbl">Predicción de cada jugador</div><div class="calc-pred-grid">';_CHANCE_PLAYERS.forEach(function(player){var pid=_calcPid(player),pShort=player.split(' ')[0];html+='<div class="calc-pred-row"><span class="calc-pred-name" title="'+player+'">'+pShort+'</span><input type="number" class="calc-score-inp calc-p-inp" id="'+m.id+'-p-'+pid+'-1" min="0" max="15" placeholder="?" oninput="_calcUpdate()"><span class="calc-sep"> − </span><input type="number" class="calc-score-inp calc-p-inp" id="'+m.id+'-p-'+pid+'-2" min="0" max="15" placeholder="?" oninput="_calcUpdate()"><select class="calc-cls-sel calc-cls-sm" id="'+m.id+'-p-'+pid+'-cls" onchange="_calcUpdate()"><option value="">—</option>';m.teams.forEach(function(t){html+='<option value="'+t+'">'+t.substring(0,4)+'</option>';});html+='</select></div>';});html+='</div></div>';});html+='<div class="calc-bonus-block"><div class="calc-match-title">✨ Bonus pre-torneo</div>';var bonusDefs=[{bid:"B1",lbl:"Campeón (+12 pts)",opts:["Argentina","España"]},{bid:"B3",lbl:"Goleador (+8 pts)",opts:["Kane","Mbappe","Julian Alvarez","Messi"]},{bid:"B4",lbl:"Más goles a favor (+5 pts)",opts:["Argentina","España","Francia"]}];bonusDefs.forEach(function(bd){html+='<div class="calc-section-lbl">'+bd.bid+' — '+bd.lbl+'</div><div class="calc-bonus-btns" style="margin-bottom:8px">';bd.opts.forEach(function(opt){html+='<button class="calc-bon-btn" data-cbid="'+bd.bid+'" data-cbval="'+opt+'">'+opt.split(" ")[0]+'</button>';});html+='<button class="calc-bon-btn active" data-cbid="'+bd.bid+'" data-cbval="">—</button></div>';});html+='<div style="margin-top:6px;font-size:.6rem;color:var(--muted)">B2 Subcampeón se deriva automáticamente. B5/B6: nadie puede ganarlos.</div></div>';panel.innerHTML=html;panel.querySelectorAll('[data-cbid]').forEach(function(btn){btn.addEventListener('click',function(){_calcBonusPick(this.dataset.cbid,this.dataset.cbval);});});}
function renderCalcFinal(data){_calcData=data;_calcBonusPicks={};(data.bonus_preds||[]).forEach(function(b){Object.keys(b.predictions).forEach(function(player){if(!_calcBonusPicks[player])_calcBonusPicks[player]={};_calcBonusPicks[player][b.id]=b.predictions[player]||'';});});_buildCalcPanel(data);_calcUpdate();}

// ---- RELATOR ----
var _relatorData=null;
function _fmtLine(txt,data){
  var out=txt;
  data.players.forEach(function(p){
    var c=data.colors[p]||'#ccc';
    var esc=p.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
    out=out.replace(new RegExp('('+esc+')','g'),'<span style="color:'+c+';font-weight:700">$1</span>');
  });
  return out;
}
function _genRelato(data){
  var rk=data.ranking,n=rk.length;
  var ldr=rk[0],sec=rk[1],trd=rk[2],lst=rk[n-1];
  var g12=ldr.pts-sec.pts,gBot=ldr.pts-lst.pts;
  var players=data.players,N=players.length;
  var ko=data.knockout_matches||[];
  var koPlayed=ko.filter(function(m){return m.played;});
  // Detect current phase (last phase that has played matches)
  var curPhase='Grupos';
  ['16avos','Octavos','Cuartos','Semis','3er Puesto','Final'].forEach(function(ph){
    if(koPlayed.some(function(m){return m.phase===ph;}))curPhase=ph;
  });
  function phMs(ph){return koPlayed.filter(function(m){return m.phase===ph;});}
  var ph16=phMs('16avos'),phOct=phMs('Octavos'),phCua=phMs('Cuartos'),phSem=phMs('Semis');
  function sumPts(ms){var r={};players.forEach(function(p){r[p]=0;});ms.forEach(function(m){players.forEach(function(p){r[p]+=(m.points[p]||0);});});return r;}
  var koPts=sumPts(koPlayed),pts16=sumPts(ph16),ptsOct=sumPts(phOct),ptsCua=sumPts(phCua);
  function topOf(d){return players.slice().sort(function(a,b){return d[b]-d[a];})[0];}
  function botOf(d){return players.slice().sort(function(a,b){return d[a]-d[b];})[0];}
  var upsets=koPlayed.filter(function(m){return players.filter(function(p){return(m.points[p]||0)>0;}).length<=Math.floor(N*0.3);});
  var formD=rk.map(function(r){
    var hist=data.history[r.name]||[0],d=[];
    for(var i=1;i<hist.length;i++)d.push(hist[i]-hist[i-1]);
    return{name:r.name,pts:r.pts,last5:d.slice(-5).reduce(function(a,b){return a+b;},0)};
  });
  var bf=formD.slice().sort(function(a,b){return b.last5-a.last5;})[0];
  var lines=[];
  // Apertura: contexto de fase actual
  if(curPhase==='Grupos'){
    lines.push('Fase de grupos en curso. El eliminatorio aun no arranco — este relato refleja el estado de los '+data.matches_played.length+' partidos de grupos registrados.');
  } else if(curPhase==='16avos'){
    var done16=ph16.length===16;
    lines.push(_pick([
      (done16?'16avos de final completados (16/16). ':'16avos en curso: '+ph16.length+'/16 jugados. ')+'El primer filtro eliminatorio del Mundial 2026 — este formato de 48 selecciones lo estrena como fase oficial. Exacto vale 5pts, acertar la direccion da 2pts, clasificado +2.',
      (done16?'16avos cerrados. ':'16avos: '+ph16.length+' de 16 jugados. ')+'Primera fase knock-out del torneo mas grande de la historia. Los 32 mejores del grupo de 48 avanzaron hasta aca — empieza el cuadro definitivo.',
    ]));
  } else if(curPhase==='Octavos'){
    var doneOct=phOct.length===8;
    lines.push(_pick([
      (doneOct?'Octavos completados. ':'Octavos en curso: '+phOct.length+'/8 jugados. ')+'Los 16avos ya definieron quienes sobrevivieron. En Octavos el valor sube: exacto 7pts, acertar la direccion 3pts, clasificado +2.',
      (doneOct?'Octavos cerrados — el torneo entra en Cuartos de final. ':'Octavos: '+phOct.length+'/8 jugados. ')+'Cada partido que pasa es un resultado que ya no se puede recuperar en el prode.',
    ]));
  } else if(curPhase==='Cuartos'){
    var doneCua=phCua.length===4;
    // Exactos en Cuartos
    var cuaExactCnt={};
    players.forEach(function(p){cuaExactCnt[p]=0;});
    phCua.forEach(function(m){players.forEach(function(p){if((m.points[p]||0)>=7)cuaExactCnt[p]++;});});
    var cuaExactos=players.filter(function(p){return cuaExactCnt[p]>0;});
    if(doneCua){
      lines.push(_pick([
        'CUARTOS DE FINAL COMPLETADOS. Francia, Espana, Inglaterra y Argentina avanzan a Semifinales. Cuatro potencias, dos llaves, y el prode llega a su tramo definitivo.',
        'Cuartos cerrados. Semis definidas: Francia vs Espana, e Inglaterra vs Argentina. De 48 selecciones, quedan 4. Esto es el Mundial.',
      ]));
      if(cuaExactos.length>0){
        var exactoStrs=cuaExactos.map(function(p){return p+' ('+cuaExactCnt[p]+' exacto'+(cuaExactCnt[p]>1?'s':'')+')'});
        lines.push('Exactos en Cuartos: '+exactoStrs.join(', ')+'. A 7 pts por exacto mas 2 por clasificado — esos aciertos reordenaron la tabla de manera decisiva.');
      }
      lines.push('El torneo sorprendio en el camino: Noruega elimino a Brasil, Belgica a USA, Espana a Portugal. La tabla del prode absorbio esas divergencias. Quien apostaba a los favoritos clásicos sufrio; quien leyó el torneo, escalo.');
    } else {
      lines.push('Cuartos en curso: '+phCua.length+'/4 jugados. Solo 8 equipos quedan. Cada resultado puede mover la tabla mas que diez jornadas de grupos.');
    }
  } else if(curPhase==='Semis'){
    var doneSem=phSem.length===2;
    var semExactCnt={};
    players.forEach(function(p){semExactCnt[p]=0;});
    phSem.forEach(function(m){players.forEach(function(p){if((m.points[p]||0)>=7)semExactCnt[p]++;});});
    var semExactos=players.filter(function(p){return semExactCnt[p]>0;});
    if(doneSem){
      lines.push(_pick([
        'SEMIFINALES COMPLETADAS. Argentina y España van a la Gran Final — el cruce soñado. Tomi Marchiano lidera con '+ldr.pts+' pts pero SIN bonuses disponibles: su techo es 270. Hay 8 jugadores que matematicamente pueden superarlo. La Final lo decide todo.',
        'Semis cerradas. FINAL: Argentina vs España. La mejor noticia para el prode: el lider (Tomi, '+ldr.pts+' pts) no tiene bonuses. Su maximo es 270. Los que apostaron a Argentina o España en B1 todavia pueden ganar.',
      ]));
      if(semExactos.length>0){
        var semExStr=semExactos.map(function(p){return p+' ('+semExactCnt[p]+' exacto'+(semExactCnt[p]>1?'s':'')+')'});
        lines.push('Exactos en Semis: '+semExStr.join(', ')+'. A 7 pts cada uno — aciertos que remezclaron la tabla en el tramo final.');
      }
      lines.push('Con 9 jugadores con chance matematica (max > 270), la Final argentina-española es la mas decisiva de la historia del Prode Toros. Exacto en Final vale 10 pts, clasificado +2, goleada +5 — hasta 17 pts en un partido. El lider puede caer.');
    } else {
      lines.push('Semis en curso: '+phSem.length+'/2 jugados. Argentina y Francia juegan mañana. Los que apostaron a Argentina o España en bonuses todavia tienen todo para ganar.');
      if(semExactos.length>0){
        var semExStr2=semExactos.map(function(p){return p+' ('+semExactCnt[p]+' exacto'+(semExactCnt[p]>1?'s':'')+')'});
        lines.push('Exactos en Semis hasta ahora: '+semExStr2.join(', ')+'. Cada exacto a 7 pts cambia el orden.');
      }
    }
  } else if(curPhase==='Final'||curPhase==='3er Puesto'){
    lines.push('LA GRAN FINAL. Argentina vs España — el ultimo partido del Prode Toros 2026. Todo puede cambiar. Max disponible: 17 pts en la Final + 12 pts en 3er Puesto + bonuses. El ganador del prode se decide aqui.');
  } else {
    lines.push('El torneo cerro. Este relato resume el Prode Toros 2026 completo.');
  }
  // Ranking actual
  var rk4=rk.slice(0,4).map(function(r){return r.name+' '+r.pts;}).join(' · ');
  if(g12===0){
    lines.push(ldr.name+' y '+sec.name+' igualados en la cima con '+ldr.pts+' pts. Empate exacto — el proximo partido los separa o los mantiene juntos. '+trd.name+' acecha en 3ro con '+trd.pts+'.');
  } else if(g12<=5){
    lines.push(ldr.name+' lidera con '+ldr.pts+' pts, solo '+g12+' sobre '+sec.name+' ('+sec.pts+'). Con 3 partidos restantes (Semis + Final + 3ero), un exacto vale 7 o 10 pts. La diferencia se borra en un partido. Top 4: '+rk4+'.');
  } else if(g12<=15){
    lines.push(ldr.name+' en la cima con '+ldr.pts+' pts y '+g12+' sobre '+sec.name+' ('+sec.pts+'). Ventaja real, pero en Semis y Final hay 24-30 pts en juego — nada esta definido. Top 4: '+rk4+'.');
  } else {
    lines.push(ldr.name+' lidera con '+ldr.pts+' pts, '+g12+' sobre '+sec.name+' ('+sec.pts+'). Margen solido, pero los ultimos partidos concentran los puntos maximos del torneo. Top 4: '+rk4+'.');
  }
  // Analisis por fase knockout
  if(koPlayed.length>0){
    if(ph16.length>0){
      var t16=topOf(pts16),b16=botOf(pts16);
      if(ph16.length===16){
        lines.push('16avos completos: '+t16+' fue el mejor de la fase con '+pts16[t16]+' pts; '+b16+' el mas bajo con '+pts16[b16]+'. Diferencia de '+(pts16[t16]-pts16[b16])+' pts generada solo en los 16avos — el primer paso de divergencia en el cuadro.');
      } else {
        lines.push('16avos ('+ph16.length+'/16 jugados): '+t16+' lidera la fase con '+pts16[t16]+' pts, '+b16+' con '+pts16[b16]+'. Restan '+(16-ph16.length)+' partidos de la primera ronda.');
      }
    }
    if(phOct.length>0){
      var tOct=topOf(ptsOct),bOct=botOf(ptsOct);
      if(phOct.length===8){
        lines.push('Octavos cerrados: '+tOct+' domino la fase con '+ptsOct[tOct]+' pts; '+bOct+' con '+ptsOct[bOct]+'. Diferencia acumulada en Octavos: '+(ptsOct[tOct]-ptsOct[bOct])+' pts.');
      } else {
        lines.push('Octavos en curso ('+phOct.length+'/8): '+tOct+' lidera la fase con '+ptsOct[tOct]+' pts; '+bOct+' con '+ptsOct[bOct]+'. Restan '+(8-phOct.length)+' partido'+(8-phOct.length!==1?'s':'')+' de esta ronda.');
      }
    }
    if(phCua.length>0){
      var tCua=topOf(ptsCua),bCua=botOf(ptsCua);
      if(phCua.length===4){
        lines.push('Cuartos cerrados: '+tCua+' fue el mejor de la fase con '+ptsCua[tCua]+' pts; '+bCua+' el mas bajo con '+ptsCua[bCua]+'. Diferencia generada solo en Cuartos: '+(ptsCua[tCua]-ptsCua[bCua])+' pts.');
      } else {
        lines.push('Cuartos en curso ('+phCua.length+'/4): '+tCua+' lidera la fase con '+ptsCua[tCua]+' pts; '+bCua+' con '+ptsCua[bCua]+'. Cada resultado puede reshapear la tabla de manera drastica.');
      }
    }
    var koLdr=topOf(koPts);
    lines.push(_pick([
      koLdr+' lidera el eliminatorio acumulando '+koPts[koLdr]+' pts desde los 16avos. El desempeno en el KO es la variable nueva del prode — quien acierta clasificados y marcadores exactos aqui es quien define la tabla.',
      'Mejor rendimiento en partidos eliminatorios hasta ahora: '+koLdr+' con '+koPts[koLdr]+' pts en el KO. Cada jornada del eliminatorio mueve la tabla mas que tres jornadas de grupos.',
    ]));
    if(upsets.length>0){
      lines.push('Sorpresa'+(upsets.length>1?'s':'')+' del eliminatorio: '+upsets.map(function(m){return m.match;}).join(', ')+'. '+(upsets.length>1?'En esos partidos':'Ahi')+' menos del 30% acerto la direccion — los puntos quedaron concentrados en pocos jugadores.');
    }
  }
  // Forma reciente (ultimas 5 jornadas combinadas)
  if(bf&&bf.last5>0){
    lines.push(_pick([
      bf.name+' tiene el mejor rendimiento en los ultimos 5 partidos con '+bf.last5+' pts. Momento de forma que puede ser clave en las fases que quedan.',
      'Ultimas 5 jornadas: '+bf.name+' en racha con '+bf.last5+' pts. La forma reciente es el indicador mas fresco del estado del prode en este momento.',
    ]));
  }
  // Fondo de tabla
  lines.push(_pick([
    lst.name+' cierra la tabla con '+lst.pts+' pts, a '+gBot+' del lider. En Semis y Final todavia hay mas de 30 pts disponibles — la remontada matematica existe, pero requiere exactos propios y fallos de los de arriba en simultaneo.',
    'Puesto '+n+': '+lst.name+' con '+lst.pts+' pts. La diferencia es '+gBot+'. El volumen de la recta final puede subvertir la tabla, pero hay que acertar exactos mientras los lideres fallan.',
  ]));
  // Cierre
  lines.push(_pick([
    'Quedan 2 partidos: 3er Puesto y Final. Max posible: 17 pts en Final + 12 en 3er Puesto + hasta 33 pts en bonuses. El prode Toros puede cambiar de dueño en 90 minutos.',
    '3er Puesto y Final — los dos partidos que cierran el torneo. Exacto en Final vale 10 pts (+5 goleada, +2 cls). Con 9 jugadores matematicamente vivos, la distribucion de bonuses y un exacto pueden voltear la tabla completa.',
  ]));
  return lines;
}
function _relateNow(){
  if(!_relatorData)return;
  var body=document.getElementById('relator-body');
  body.innerHTML='';
  var lines=_genRelato(_relatorData);
  lines.forEach(function(line,i){
    var el=document.createElement('div');
    el.className='relator-line';
    el.style.animationDelay=(i*0.13)+'s';
    el.innerHTML=_fmtLine(line,_relatorData);
    body.appendChild(el);
  });
}
function renderFases(data){
  var players=data.players,colors=data.colors;
  var PHASES=['Grupos','16avos','Octavos','Cuartos','Semis','3er Puesto','Final'];
  var PHASE_LABELS={'Grupos':'Grupos','16avos':'16avos','Octavos':'Octavos','Cuartos':'Cuartos','Semis':'Semis','3er Puesto':'3er Puesto','Final':'Final'};

  // Calcular puntos por fase
  var pp={};
  PHASES.forEach(function(ph){pp[ph]={};players.forEach(function(p){pp[ph][p]=0;});});
  (data.group_preds||[]).forEach(function(m){
    players.forEach(function(p){pp['Grupos'][p]+=(m.pts[p]||0);});
  });
  (data.knockout_matches||[]).filter(function(m){return m.played;}).forEach(function(m){
    if(pp[m.phase])players.forEach(function(p){pp[m.phase][p]+=(m.points[p]||0);});
  });

  // Estado de cada fase
  var ko=data.knockout_matches||[];
  function phaseStatus(ph){
    if(ph==='Grupos')return(data.group_preds||[]).length>0?'done':'upcoming';
    var ms=ko.filter(function(m){return m.phase===ph;});
    if(!ms.length)return'upcoming';
    var played=ms.filter(function(m){return m.played;}).length;
    if(played===0)return'upcoming';
    if(played===ms.length)return'done';
    return'active';
  }

  // Partidos por dia en knockout
  var dayMap={};
  ko.filter(function(m){return m.played&&m.match_date;}).forEach(function(m){
    if(!dayMap[m.match_date])dayMap[m.match_date]=[];
    dayMap[m.match_date].push(m);
  });

  function fmtDate(d){var p=d.split('-');var meses=['','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];return p[2]+' '+meses[parseInt(p[1])];}

  function chipCls(pts,phase){
    var ex=phase==='Final'?10:phase==='Grupos'?5:7;
    var cm=phase==='Final'?5:phase==='Grupos'?2:3;
    if(!pts)return'dsc-miss';
    // pts exacto+bonus tiene 2 mas que exacto
    if(pts===ex+2||pts===cm+2)return'dsc-bonus';
    if(pts>=ex)return'dsc-exact';
    return'dsc-common';
  }

  function renderPhaseContent(ph){
    var pts=pp[ph];
    var status=phaseStatus(ph);
    if(status==='upcoming'){
      return'<div class="phase-upcoming-msg">Fase aun no comenzada &mdash; los datos apareceran cuando se juegue el primer partido</div>';
    }
    // Leaderboard
    var sorted=players.slice().sort(function(a,b){return pts[b]-pts[a];});
    var maxPts=pts[sorted[0]]||1;
    var posLabels=['p1','p2','p3'];
    var html='<div class="phase-lead-title">Puntos acumulados en fase</div>';
    sorted.forEach(function(p,i){
      var v=pts[p],pct=Math.round(v/maxPts*100),c=colors[p]||'#ccc';
      var pc=i<3?posLabels[i]:'';
      html+='<div class="phase-row"><div class="phase-pos '+pc+'">'+(i+1)+'</div>';
      html+='<div class="phase-name"><span class="clr-dot" style="background:'+c+'"></span>'+p+'</div>';
      html+='<div class="phase-pts-val" style="color:'+c+'">'+v+'</div>';
      html+='<div class="phase-bar-wrap"><div class="phase-bar-fill" style="width:'+pct+'%;background:'+c+'"></div></div></div>';
    });

    // By-day (solo knockout)
    if(ph!=='Grupos'){
      var days=Object.keys(dayMap).filter(function(d){
        return dayMap[d].some(function(m){return m.phase===ph;});
      }).sort();
      days.forEach(function(day){
        var matches=dayMap[day].filter(function(m){return m.phase===ph;});
        if(!matches.length)return;
        html+='<div class="day-group"><div class="day-header">&#128197; '+fmtDate(day)+'</div>';
        matches.forEach(function(m){
          html+='<div class="day-match-row"><div class="day-match-name">'+m.match+'</div><div class="day-match-scores">';
          var grouped={};
          players.forEach(function(p){
            var v=m.points[p]||0;
            var cls=chipCls(v,ph);
            if(!grouped[cls+'-'+v])grouped[cls+'-'+v]={cls:cls,pts:v,names:[]};
            grouped[cls+'-'+v].names.push(p);
          });
          Object.keys(grouped).sort(function(a,b){return grouped[b].pts-grouped[a].pts;}).forEach(function(k){
            var g=grouped[k];
            html+='<span class="day-score-chip '+g.cls+'" title="'+g.names.join(', ')+'">'+g.pts+'pts &times;'+g.names.length+'</span>';
          });
          html+='</div></div>';
        });
        html+='</div>';
      });
    }
    return html;
  }

  // Tabs
  var firstActive='Grupos';
  var tabsHtml='';
  PHASES.forEach(function(ph){
    var st=phaseStatus(ph);
    var cls='phase-tab'+(st==='done'?' done':st==='upcoming'?' upcoming':'');
    var badge=st==='done'?'<span class="phase-badge" style="color:var(--green)">&#10003;</span>':
               st==='active'?'<span class="phase-badge" style="color:var(--cyan)">&#9679;</span>':'';
    if(st==='active')firstActive=ph;
    tabsHtml+='<button class="'+cls+'" data-phase="'+ph+'">'+PHASE_LABELS[ph]+badge+'</button>';
  });
  document.getElementById('phase-tabs').innerHTML=tabsHtml;

  // Contenidos
  var contentsEl=document.getElementById('phase-contents');
  contentsEl.innerHTML='';
  PHASES.forEach(function(ph){
    var div=document.createElement('div');
    div.className='phase-content';
    div.id='phase-cnt-'+ph.replace(/\s/g,'-');
    div.innerHTML=renderPhaseContent(ph);
    contentsEl.appendChild(div);
  });

  // Activar primera tab con datos
  function activateTab(ph){
    document.querySelectorAll('.phase-tab').forEach(function(t){
      t.classList.toggle('active',t.dataset.phase===ph);
    });
    document.querySelectorAll('.phase-content').forEach(function(c){
      c.classList.toggle('active',c.id==='phase-cnt-'+ph.replace(/\s/g,'-'));
    });
  }
  activateTab(firstActive);
  document.querySelectorAll('.phase-tab').forEach(function(btn){
    btn.addEventListener('click',function(){activateTab(this.dataset.phase);});
  });
}

function renderBonus(data){
  var players=data.players,colors=data.colors,bp=data.bonus_preds||[];
  if(!bp.length){
    document.getElementById('bonus-body').innerHTML='<p style="color:var(--muted);padding:20px">Sin datos de bonus.</p>';
    return;
  }

  // Alive predictions per bonus (normalized, accent-insensitive)
  var _BONUS_ALIVE_MAP={
    'B1':['argentina','espana'],'B2':['argentina','espana'],
    'B3':['kane','mbappe','julian alvarez','messi'],
    'B4':['espana','argentina','francia'],'B5':[],'B6':[]
  };
  function _bn(s){return(s||'').trim().toLowerCase().replace(/á/g,'a').replace(/é/g,'e').replace(/í/g,'i').replace(/ó/g,'o').replace(/ú/g,'u').replace(/ñ/g,'n');}
  function _isAlive(bid,pred){var alive=_BONUS_ALIVE_MAP[bid]||[];return alive.length===0?false:alive.some(function(a){return _bn(pred)===a||_bn(pred).includes(a)||a.includes(_bn(pred).split(' ')[0]);});}

  // Totales por jugador
  var totals={};players.forEach(function(p){totals[p]=0;});
  bp.forEach(function(b){players.forEach(function(p){totals[p]+=(b.earned[p]||0);});});
  var maxPts=bp.reduce(function(s,b){return s+b.pts_value;},0);

  var html='<div class="bonus-intro">Predicciones realizadas antes de que comenzara el torneo. Puntos se acreditan cuando se confirme el resultado final &mdash; max. posible: <strong>'+maxPts+' pts</strong>. <span style="color:var(--pink)">&#10060;</span> = prediccion eliminada.</div>';

  // Detalle por categoria
  html+='<div style="margin-top:36px">';
  var ICONS={'Campeon del Mundial':'&#127942;','Subcampeon':'&#129352;','Goleador del torneo':'&#9917;','Sel. mas goles a favor':'&#128293;','Sel. mas goles en contra':'&#129505;'};
  bp.forEach(function(b){
    var icon=ICONS[b.label]||'&#127381;';
    var bid=b.id;
    // Agrupar jugadores por prediccion
    var groups={};
    players.forEach(function(p){
      var pred=b.predictions[p]||'—';
      if(!groups[pred])groups[pred]=[];
      groups[pred].push(p);
    });
    var sortedGroups=Object.keys(groups).sort(function(a,b2){return groups[b2].length-groups[a].length;});

    html+='<div class="day-group"><div class="day-header">'+icon+' '+b.label+' <span class="phase-badge" style="color:var(--gold);font-size:.75rem;font-weight:700">+'+b.pts_value+' pts</span>';
    var earnedAny=players.some(function(p){return(b.earned[p]||0)>0;});
    if(earnedAny){html+=' <span style="color:var(--green);font-size:.72rem">&#10003; Acreditado</span>';}
    else{html+=' <span style="color:var(--muted);font-size:.68rem">Pendiente</span>';}
    html+='</div>';

    html+='<div style="display:flex;flex-wrap:wrap;gap:10px 20px;padding:6px 0 4px">';
    sortedGroups.forEach(function(pred){
      var ps=groups[pred];
      var isGroupAlive=_isAlive(bid,pred);
      var predColor=isGroupAlive?'var(--text)':'var(--muted)';
      var predPrefix=isGroupAlive?'':'<span style="color:var(--pink);margin-right:2px">&#10060;</span>';
      html+='<div style="min-width:120px;'+(isGroupAlive?'':'opacity:.55')+'" ><div style="font-size:.7rem;font-weight:700;color:'+predColor+';margin-bottom:4px">'+predPrefix+pred+' <span style="color:var(--muted);font-weight:400">('+ps.length+')</span></div>';
      html+='<div style="display:flex;flex-wrap:wrap;gap:3px">';
      ps.forEach(function(p){
        var c=colors[p]||'#ccc';
        var earned=(b.earned[p]||0)>0;
        html+='<span class="bonus-chip" style="border-color:'+(earned?'var(--green)':isGroupAlive?'rgba(255,215,0,.25)':'rgba(255,64,129,.2)')+';color:'+(earned?'var(--green)':isGroupAlive?c:'rgba(255,64,129,.5)')+'">'+(earned?'&#10003; ':'')+p.split(' ')[0]+'</span>';
      });
      html+='</div></div>';
    });
    html+='</div></div>';
  });
  html+='</div>';

  document.getElementById('bonus-body').innerHTML=html;
}

function renderRelator(data){_relatorData=data;document.getElementById('relator-btn').onclick=_relateNow;}

function renderBadges(data){
  var players=data.players,colors=data.colors,N=players.length;
  var gp=data.group_preds||[];
  var st={};
  players.forEach(function(p){
    var hist=data.history[p]||[0],d=[];
    for(var i=1;i<hist.length;i++)d.push(hist[i]-hist[i-1]);
    var tot=d.length||1, pts=data.ranking.find(function(r){return r.name===p;}).pts;
    var mean=pts/tot;
    var variance=d.reduce(function(s,x){return s+(x-mean)*(x-mean);},0)/tot;
    var hardPts=0,hardN=0;
    gp.forEach(function(m){
      var ac=players.filter(function(q){return(m.pts[q]||0)>0;}).length;
      if(ac<=Math.floor(N*0.3)){hardN++;hardPts+=(m.pts[p]||0);}
    });
    st[p]={
      exactos:d.filter(function(x){return x>=5;}).length,
      misses:d.filter(function(x){return!x;}).length,
      last20:d.slice(-20).reduce(function(a,b){return a+b;},0),
      first20:d.slice(0,20).reduce(function(a,b){return a+b;},0),
      stddev:Math.sqrt(variance),avg:mean,hardPts:hardPts,hardN:hardN
    };
  });
  var defs=[
    {icon:'&#127919;',name:'El Francotirador',desc:'Mas resultados exactos en la fase de grupos',key:'exactos',asc:false,fmt:function(v){return v+' exactos';}},
    {icon:'&#128208;',name:'El Reloj Suizo',desc:'Mayor consistencia — menor varianza entre partidos',key:'stddev',asc:true,fmt:function(v){return '&sigma;='+v.toFixed(2)+' (menor=mas consistente)';}},
    {icon:'&#128176;',name:'El Cobrador',desc:'Mas puntos en partidos donde &le;30% acerto la direccion',key:'hardPts',asc:false,fmt:function(v,p){return v+' pts en '+st[p].hardN+' partidos dificiles';}},
    {icon:'&#128293;',name:'El Cerrero',desc:'Mejor rendimiento en los ultimos 20 partidos de grupos',key:'last20',asc:false,fmt:function(v){return v+' pts (ult. 20)';}},
    {icon:'&#128640;',name:'El Arrancador',desc:'Mayor puntaje en los primeros 20 partidos de grupos',key:'first20',asc:false,fmt:function(v){return v+' pts (prim. 20)';}},
    {icon:'&#129396;',name:'El Sufridor',desc:'Mas partidos sin puntuar — el que mas pago el plato',key:'misses',asc:false,fmt:function(v){return v+' misses';}},
    {icon:'&#129504;',name:'El Analitico',desc:'Mayor promedio de puntos por partido jugado',key:'avg',asc:false,fmt:function(v){return v.toFixed(2)+' pts/partido';}},
  ];
  var html='<div class="badges-section-lbl">Fase de Grupos</div><div class="badges-grid">';
  defs.forEach(function(def){
    var sorted=players.slice().sort(function(a,b){
      return def.asc?(st[a][def.key]-st[b][def.key]):(st[b][def.key]-st[a][def.key]);
    });
    var winner=sorted[0],val=st[winner][def.key],c=colors[winner]||'#ccc';
    html+='<div class="badge-card">';
    html+='<div class="badge-icon">'+def.icon+'</div>';
    html+='<div class="badge-title">'+def.name+'</div>';
    html+='<div class="badge-desc">'+def.desc+'</div>';
    html+='<div class="badge-winner" style="color:'+c+'">'+winner+'</div>';
    html+='<div class="badge-stat">'+def.fmt(val,winner)+'</div>';
    html+='</div>';
  });
  html+='</div>';
  // Seccion Eliminatorio
  var kp=data.ko_preds||[];
  if(kp.length>0){
    var koTot={},koDirOk={},koSurpPts={},koExactN={};
    players.forEach(function(p){koTot[p]=0;koDirOk[p]=0;koSurpPts[p]=0;koExactN[p]=0;});
    var koEt={'16avos':5,'Octavos':7,'Cuartos':7,'Semis':7,'3er Puesto':7,'Final':10};
    kp.forEach(function(m){
      var correct=players.filter(function(p){return(m.pts[p]||0)>0;}).length;
      var isSurp=correct<=Math.floor(N*0.3);
      var et=koEt[m.phase]||5;
      players.forEach(function(p){
        var pts=m.pts[p]||0;
        koTot[p]+=pts;
        if(pts>0)koDirOk[p]++;
        if(isSurp)koSurpPts[p]+=pts;
        if(pts>=et)koExactN[p]++;
      });
    });
    function koBest(obj){return players.slice().sort(function(a,b){return obj[b]-obj[a];})[0];}
    var koDefs=[
      {icon:'&#127942;',name:'Rey del Eliminatorio',desc:'Mas puntos acumulados en partidos KO hasta ahora ('+kp.length+' jugados)',obj:koTot,fmt:function(p){return koTot[p]+' pts en KO';}},
      {icon:'&#128175;',name:'El Sorpresero',desc:'Mas puntos en partidos donde &le;30% acerto la direccion',obj:koSurpPts,fmt:function(p){return koSurpPts[p]+' pts en sorpresas';}},
      {icon:'&#127919;',name:'Certero en KO',desc:'Mas veces que acerto la direccion del resultado en el eliminatorio',obj:koDirOk,fmt:function(p){return koDirOk[p]+'/'+kp.length+' direcciones OK';}},
      {icon:'&#129354;',name:'Exacto en KO',desc:'Mas marcadores exactos en el cuadro eliminatorio',obj:koExactN,fmt:function(p){return koExactN[p]+' exacto'+(koExactN[p]!==1?'s':'')+' KO';}},
    ];
    html+='<div class="badges-section-lbl ko">&#9889; Eliminatorio <span class="badges-section-sub">'+kp.length+' partido'+(kp.length!==1?'s':'')+' jugados</span></div>';
    html+='<div class="badges-grid">';
    koDefs.forEach(function(def){
      var winner=koBest(def.obj),c=colors[winner]||'#ccc';
      html+='<div class="badge-card ko-badge">';
      html+='<div class="badge-icon">'+def.icon+'</div>';
      html+='<div class="badge-title">'+def.name+'</div>';
      html+='<div class="badge-desc">'+def.desc+'</div>';
      html+='<div class="badge-winner" style="color:'+c+'">'+winner+'</div>';
      html+='<div class="badge-stat">'+def.fmt(winner)+'</div>';
      html+='</div>';
    });
    html+='</div>';
  }
  document.getElementById('badges-body').innerHTML=html;
}

function renderMatrix(data){
  var players=data.players,colors=data.colors,N=players.length;
  var gp=data.group_preds||[],kp=data.ko_preds||[];
  if(!gp.length&&!kp.length){document.getElementById('matrix-body').innerHTML='<p style="color:var(--muted);padding:20px">Sin datos de predicciones.</p>';return;}
  var abbr=function(n){return n.split(' ')[0].substring(0,7);};
  var koEt={'16avos':5,'Octavos':7,'Cuartos':7,'Semis':7,'3er Puesto':7,'Final':10};
  var html='<div class="matrix-legend">';
  html+='<span class="mx-leg"><span class="mx-leg-dot" style="background:rgba(63,185,80,.4)"></span>Exacto</span>';
  html+='<span class="mx-leg"><span class="mx-leg-dot" style="background:rgba(255,215,0,.3)"></span>Comun</span>';
  html+='<span class="mx-leg"><span class="mx-leg-dot" style="background:rgba(255,64,129,.2)"></span>Fallo</span>';
  html+='<span class="mx-leg" style="color:var(--pink)">&#9679; nombre en rojo = partido dificil (&le;30% acerto)</span>';
  html+='</div>';
  html+='<div class="matrix-wrap"><table class="matrix-table"><thead><tr>';
  html+='<th class="matrix-match-col">Partido</th><th class="matrix-res-col">Resultado</th>';
  players.forEach(function(p){html+='<th class="matrix-player-col" title="'+p+'" style="color:'+(colors[p]||'#ccc')+'">'+abbr(p)+'</th>';});
  html+='</tr></thead><tbody>';
  function buildRows(matches,headerLabel,hdrCls){
    var out='<tr><td colspan="'+(N+2)+'" class="matrix-phase-hdr'+(hdrCls?' '+hdrCls:'')+'">'+headerLabel+'</td></tr>';
    matches.forEach(function(m){
      var et=m.phase?koEt[m.phase]||5:5;
      var ac=players.filter(function(p){return(m.pts[p]||0)>0;}).length;
      var diffCls=ac<=Math.floor(N*0.3)?'diff-hard':ac<=Math.floor(N*0.5)?'diff-med':'';
      var actualRes=null;
      players.forEach(function(p){if(!actualRes&&(m.pts[p]||0)>=et&&m.predictions[p])actualRes=m.predictions[p];});
      out+='<tr class="'+diffCls+'">';
      out+='<td class="matrix-match-name" title="'+m.match+'">'+m.match.replace(/ vs /g,' v ').substring(0,22)+(m.match.length>22?'&#8230;':'')+'</td>';
      out+='<td class="matrix-actual">'+(actualRes||'?')+'</td>';
      players.forEach(function(p){
        var pred=m.predictions[p],pts=m.pts[p]||0;
        var cls=pts>=et?'mx-exact':pts>0?'mx-common':'mx-miss';
        out+='<td class="matrix-cell '+cls+'" title="'+p+': '+(pred||'—')+' ('+pts+'pts)">'+(pred||'—')+'</td>';
      });
      out+='</tr>';
    });
    return out;
  }
  if(gp.length)html+=buildRows(gp,'Fase de Grupos ('+gp.length+')','');
  if(kp.length)html+=buildRows(kp,'&#9889; Eliminatorio ('+kp.length+')','ko');
  html+='</tbody></table></div>';
  document.getElementById('matrix-body').innerHTML=html;
}

function renderDifficulty(data){
  var players=data.players,gp=data.group_preds||[],kp=data.ko_preds||[],N=players.length;
  if(!gp.length&&!kp.length){document.getElementById('dificultad-body').innerHTML='<p style="color:var(--muted);padding:20px">Sin datos.</p>';return;}
  var koEt={'16avos':5,'Octavos':7,'Cuartos':7,'Semis':7,'3er Puesto':7,'Final':10};
  function buildDifSection(matches,sectionLbl,lblCls){
    var rows=matches.map(function(m){
      var et=m.phase?koEt[m.phase]||5:5;
      var ac=players.filter(function(p){return(m.pts[p]||0)>0;}).length;
      var ex=players.filter(function(p){return(m.pts[p]||0)>=et;}).length;
      var actualRes=null;
      players.forEach(function(p){if(!actualRes&&(m.pts[p]||0)>=et&&m.predictions[p])actualRes=m.predictions[p];});
      return{match:m.match,phase:m.phase||'Grupos',ac:ac,ex:ex,pct:ac/N,actualRes:actualRes};
    }).sort(function(a,b){return a.ac-b.ac;});
    var html='<div class="dif-section-lbl'+(lblCls?' '+lblCls:'')+'">'+sectionLbl+'</div>';
    html+='<table class="dif-table"><thead><tr>';
    html+='<th>#</th><th>Partido</th><th>Fase</th><th>Resultado</th><th>Acertaron</th><th>Exactos</th><th>Dificultad</th>';
    html+='</tr></thead><tbody>';
    rows.forEach(function(m,i){
      var barW=Math.round((1-m.pct)*100);
      var label=m.pct<=0.25?'&#128308; Muy dificil':m.pct<=0.5?'&#128992; Dificil':m.pct<=0.75?'&#128993; Moderado':'&#128994; Facil';
      html+='<tr>';
      html+='<td><span class="dif-rank-badge">'+(i+1)+'</span></td>';
      html+='<td class="dif-match">'+m.match+'</td>';
      html+='<td class="dif-result" style="font-size:.7rem;color:var(--muted)">'+m.phase+'</td>';
      html+='<td class="dif-result">'+(m.actualRes||'—')+'</td>';
      html+='<td class="dif-num">'+m.ac+'/'+N+'</td>';
      html+='<td class="dif-num">'+m.ex+'</td>';
      html+='<td class="dif-bar-cell"><div class="dif-bar"><div class="dif-fill" style="width:'+barW+'%"></div></div><span class="dif-label">'+label+'</span></td>';
      html+='</tr>';
    });
    html+='</tbody></table>';
    return html;
  }
  var html='';
  if(gp.length)html+=buildDifSection(gp,'Fase de Grupos','');
  if(kp.length)html+=buildDifSection(kp,'&#9889; Eliminatorio','ko');
  document.getElementById('dificultad-body').innerHTML=html;
}

function initNav(){
  var mc=document.getElementById('main-content');
  var panels={sim:document.getElementById('sim-content'),relator:document.getElementById('relator-content'),badges:document.getElementById('badges-content'),matrix:document.getElementById('matrix-content'),dificultad:document.getElementById('dificultad-content')};
  var navItems=document.querySelectorAll('.nav-item');
  var sections=['section-chart','section-ranking','section-bracket','section-fases','section-bonus'];
  var dots=Array.from(document.querySelectorAll('.s-dot'));
  var mobBtns=Array.from(document.querySelectorAll('.mob-btn'));

  function showMain(target){
    mc.style.display='';
    Object.values(panels).forEach(function(p){if(p)p.style.display='none';});
    if(target){var el=document.getElementById(target);if(el)mc.scrollTo({top:el.offsetTop-1,behavior:'smooth'});}
  }
  function showPanel(panel){
    mc.style.display='none';
    Object.values(panels).forEach(function(p){if(p)p.style.display='none';});
    if(panels[panel]){panels[panel].style.display='flex';if(panel==='relator')_relateNow();}
  }
  function setActiveNav(target,panel){
    navItems.forEach(function(b){b.classList.remove('active');});
    mobBtns.forEach(function(b){b.classList.remove('active');});
    if(target){
      var nb=document.querySelector('.nav-item[data-target="'+target+'"]');if(nb)nb.classList.add('active');
      var mb=document.querySelector('.mob-btn[data-target="'+target+'"]');if(mb)mb.classList.add('active');
    } else if(panel){
      var nb=document.querySelector('.nav-item[data-panel="'+panel+'"]');if(nb)nb.classList.add('active');
      var mb=document.querySelector('.mob-btn[data-panel="'+panel+'"]');if(mb)mb.classList.add('active');
    }
  }

  // Desktop sidebar nav
  navItems.forEach(function(btn){
    btn.addEventListener('click',function(){
      var panel=this.dataset.panel,target=this.dataset.target;
      setActiveNav(target,panel);
      if(panel)showPanel(panel); else if(target)showMain(target);
    });
  });

  // Section dots
  dots.forEach(function(dot,i){
    dot.addEventListener('click',function(){
      setActiveNav(sections[i],null);
      showMain(sections[i]);
    });
  });

  // Mobile bottom nav
  mobBtns.forEach(function(btn){
    btn.addEventListener('click',function(){
      var panel=this.dataset.panel,target=this.dataset.target;
      setActiveNav(target,panel);
      if(panel)showPanel(panel); else if(target)showMain(target);
    });
  });

  // Keyboard: arrow keys / PgUp PgDn jump between sections
  document.addEventListener('keydown',function(e){
    if(mc.style.display==='none')return;
    if(e.key!=='ArrowDown'&&e.key!=='ArrowUp'&&e.key!=='PageDown'&&e.key!=='PageUp')return;
    e.preventDefault();
    var sc=mc.scrollTop,cur=0;
    sections.forEach(function(id,i){var el=document.getElementById(id);if(el&&sc>=el.offsetTop-80)cur=i;});
    var nxt=e.key==='ArrowDown'||e.key==='PageDown'?Math.min(cur+1,sections.length-1):Math.max(cur-1,0);
    var el=document.getElementById(sections[nxt]);
    if(el)mc.scrollTo({top:el.offsetTop-1,behavior:'smooth'});
  });

  function updateActive(){
    if(mc.style.display==='none')return;
    var sc=mc.scrollTop,active=sections[0];
    sections.forEach(function(id){var el=document.getElementById(id);if(el&&sc>=el.offsetTop-80)active=id;});
    document.querySelectorAll('.nav-item[data-target]').forEach(function(btn){btn.classList.toggle('active',btn.dataset.target===active);});
    dots.forEach(function(dot,i){dot.classList.toggle('active',sections[i]===active);});
    document.querySelectorAll('.mob-btn[data-target]').forEach(function(btn){btn.classList.toggle('active',btn.dataset.target===active);});
  }
  mc.addEventListener('scroll',updateActive,{passive:true});
}

fetch('./data.json?_=' + Date.now(), {cache: 'no-store'})
  .then(function(r){if(!r.ok)throw new Error('HTTP '+r.status);return r.json();})
  .then(function(data){
    document.getElementById('loading').style.display='none';
    document.getElementById('app').style.display='flex';
    document.getElementById('footer-updated').textContent='Actualizado: '+data.last_updated;
    var ldr=data.ranking[0],sec=data.ranking[1];
    var gap=sec?(ldr.pts-sec.pts):0;
    var gapTxt=gap>0?'+'+gap+' pts sobre '+sec.name:'Empate en la cima';
    document.getElementById('leader-card').innerHTML=
      '<div class="leader-tag">&#127881;&nbsp;Va ganando...</div>'+
      '<div class="leader-name-row"><span class="clr-dot" style="background:'+(data.colors[ldr.name]||'#888')+'"></span>'+ldr.name+'</div>'+
      '<div class="leader-pts-row">'+ldr.pts+' puntos</div>'+
      '<div class="leader-gap">'+gapTxt+'</div>'+
      '<div class="leader-prize">&#129351;&nbsp;Premio: $400.000</div>';
    renderRanking(data);
    renderChart(data);
    renderBracket(data);
    renderCalcFinal(data);
    renderRelator(data);
    renderFases(data);
    renderBonus(data);
    renderBadges(data);
    renderMatrix(data);
    renderDifficulty(data);
    initNav();
  })
  .catch(function(err){document.getElementById('loading').innerHTML='<p style="color:var(--pink)">Error al cargar datos.<br><small>'+err.message+'</small></p>';});
</script>
</body>
</html>'''

with open(r'C:\Users\fedel\Desktop\bot_prode\docs\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('OK - {} chars'.format(len(html)))
