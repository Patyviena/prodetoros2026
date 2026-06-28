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
.sidebar-brand{padding:22px 20px 18px;border-bottom:1px solid var(--border);}
.brand-label{font-size:.62rem;font-weight:700;color:var(--cyan);letter-spacing:2.5px;text-transform:uppercase;margin-bottom:4px;}
.brand-title{font-size:1.4rem;font-weight:800;color:var(--text);line-height:1.1;}
.sidebar-nav{padding:10px 0;flex:1;overflow-y:auto;}
.nav-section{padding:14px 20px 6px;font-size:.58rem;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--muted);}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 20px;color:var(--muted);font-size:.88rem;font-weight:500;transition:all .15s;cursor:pointer;border:none;border-left:3px solid transparent;background:none;width:100%;text-align:left;}
.nav-item:hover{color:var(--text);background:rgba(255,255,255,.04);}
.nav-item.active{color:var(--cyan);border-left-color:var(--cyan);background:rgba(0,229,255,.05);}
.nav-item.sim-nav.active{color:var(--violet);border-left-color:var(--violet);background:rgba(179,136,255,.05);}
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
.section-bar{width:3px;height:18px;background:var(--cyan);border-radius:2px;flex-shrink:0;}
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
.rk-win-mid{color:var(--cyan);}
.rk-win-lo{color:var(--border);font-weight:400;}
.rk-form{display:flex;gap:3px;justify-content:flex-end;}
.rk-form-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;}
.rk-form-dot.miss{background:var(--border);}
.rk-form-dot.common{background:var(--green);}
.rk-form-dot.exact{background:var(--gold);}
.rk-form-dot.bonus{background:var(--gold2);}
.chart-outer{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:20px;height:520px;position:relative;}
.chart-mobile-legend{display:none;}
.reset-zoom-btn{background:rgba(0,229,255,.07);border:1px solid rgba(0,229,255,.3);color:var(--cyan);border-radius:6px;padding:6px 14px;font-size:.73rem;cursor:pointer;transition:all .2s;letter-spacing:.5px;white-space:nowrap;}
.reset-zoom-btn:hover{background:rgba(0,229,255,.14);}
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
.bm.clickable{cursor:pointer;border-color:rgba(0,229,255,.22);}
.bm.clickable:hover{background:rgba(0,229,255,.07);border-color:rgba(0,229,255,.6);transform:translateY(-1px);box-shadow:0 4px 14px rgba(0,229,255,.1);}
.bm.selected{background:rgba(0,229,255,.12);border-color:var(--cyan);box-shadow:0 0 0 1px rgba(0,229,255,.25);}
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
.bd.on{background:var(--cyan);}
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
.pg-score.local{color:var(--cyan);}
.pg-score.away{color:var(--pink);}
.pg-score.tie{color:var(--violet);}
.pg-count{font-size:.67rem;color:var(--muted);margin-bottom:5px;}
.pg-names{font-size:.7rem;color:var(--text);line-height:1.6;}
.legend-row{display:flex;gap:18px;flex-wrap:wrap;margin-bottom:24px;}
.legend-item{display:flex;align-items:center;gap:6px;font-size:.7rem;color:var(--muted);}
.legend-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.sim-content{margin-left:230px;flex:1;height:100vh;display:flex;flex-direction:column;overflow:hidden;}
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
.sim-card.has-score{border-color:rgba(0,229,255,.3);}
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
.sim-rank-row{display:grid;grid-template-columns:32px 1fr 60px 60px 70px 40px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(48,54,61,.4);gap:4px;}
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
.sim-cls-btn:hover{border-color:var(--cyan);color:var(--cyan);}
.sim-cls-btn.active{background:rgba(0,229,255,.12);border-color:var(--cyan);color:var(--cyan);font-weight:600;}
.pg-classif{font-size:.65rem;color:var(--cyan);margin-left:4px;}
.relator-content{margin-left:230px;flex:1;height:100vh;display:flex;flex-direction:column;overflow:hidden;}
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
.relator-line:first-child{border-left-color:var(--pink);font-size:1.06rem;font-weight:600;background:rgba(255,64,129,.05);}
.relator-line:last-child{border-left-color:var(--gold);background:rgba(255,215,0,.04);font-style:italic;}
@keyframes slideRelator{from{opacity:0;transform:translateX(-10px);}to{opacity:1;transform:none;}}
#loading{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:var(--bg);gap:12px;font-size:.95rem;color:var(--muted);}
.spinner{width:24px;height:24px;border:2.5px solid var(--border);border-top-color:var(--cyan);border-radius:50%;animation:spin .7s linear infinite;}
@keyframes spin{to{transform:rotate(360deg);}}
/* Section dots */
.s-dots{position:fixed;right:18px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:11px;z-index:50;}
.s-dot{width:9px;height:9px;border-radius:50%;background:var(--border);border:none;padding:0;cursor:pointer;transition:all .22s;}
.s-dot.active{background:var(--cyan);transform:scale(1.45);}
.s-dot:hover:not(.active){background:var(--muted);}
/* Sim lock */
.sim-content{position:relative;}
.sim-lock-overlay{position:absolute;inset:0;z-index:30;background:rgba(13,17,23,.97);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;text-align:center;padding:48px;pointer-events:all;}
.sim-lock-icon{font-size:3.2rem;line-height:1;}
.sim-lock-title{font-size:1.15rem;font-weight:700;}
.sim-lock-desc{font-size:.85rem;color:var(--muted);max-width:320px;line-height:1.75;}
/* Mobile bottom nav */
.mobile-bnav{display:none;position:fixed;bottom:0;left:0;right:0;background:var(--bg-card);border-top:1px solid var(--border);z-index:200;height:58px;}
.mob-btn{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6px 2px;color:var(--muted);font-size:.56rem;border:none;background:none;cursor:pointer;gap:3px;height:100%;}
.mob-btn .mi{font-size:1.1rem;}
.mob-btn.active{color:var(--cyan);}
/* Hide rank columns on mobile */
.rk-hide-mob{}
@media(max-width:800px){body{display:block;height:auto;overflow:auto;}.sidebar{display:none;}.main-content,.sim-content,.relator-content,.tool-content{margin-left:0;height:auto;}.sim-body{flex-direction:column;}.sim-left{width:100%;border-right:none;border-bottom:1px solid var(--border);}.content-section{padding:20px 14px 28px;}.relator-body,.tool-body{padding:20px 14px 62px;}.tool-header{padding:20px 14px 16px;}.mobile-bnav{display:flex;overflow-x:auto;scrollbar-width:none;gap:0;}.mobile-bnav::-webkit-scrollbar{display:none;}.mob-btn{min-width:54px;flex:0 0 auto;}.main-content,.sim-content,.relator-content,.tool-content{padding-bottom:62px;}.s-dots{display:none;}.rk-hide-mob{display:none;}.chart-outer{height:300px;padding:12px;}.chart-mobile-legend{display:flex;flex-wrap:wrap;gap:6px 12px;padding:12px 4px 0;}.cml-item{display:flex;align-items:center;gap:5px;font-size:.72rem;color:var(--muted);}.cml-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}.rk-table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:thin;scrollbar-color:var(--border) transparent;}.rk-table-wrap::-webkit-scrollbar{height:4px;}.rk-table-wrap::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px;}.rank-table{font-size:.75rem;min-width:520px;}.rank-table th,.rank-table td{padding:8px 8px;}.rk-pts{font-size:.88rem;}.rk-form{gap:2px;}.rk-form-dot{width:6px;height:6px;}.badges-grid{grid-template-columns:1fr 1fr;gap:10px;}.badge-card{padding:14px;}.dif-bar-cell{min-width:120px;}}
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
      <div class="nav-divider"></div>
      <div class="nav-section">Herramientas</div>
      <button class="nav-item sim-nav" data-panel="sim">
        <span class="nav-icon">&#128274;</span>Simulacion de Prode
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

  </main>

  <div class="sim-content" id="sim-content" style="display:none">
    <div class="sim-lock-overlay" id="sim-lock-overlay">
      <div class="sim-lock-icon">&#128274;</div>
      <div class="sim-lock-title">Simulador bloqueado</div>
      <div class="sim-lock-desc">Disponible cuando todos completen la planilla. Asi todos juegan con la misma info.</div>
    </div>
    <div class="sim-header">
      <div class="sim-title-block">
        <div class="sim-title"><div class="section-bar" style="background:var(--violet)"></div>Simulacion de Prode</div>
        <div class="sim-subtitle">Ingresa resultados y ve como queda la tabla &nbsp;&middot;&nbsp; Encontra la combinacion para ganar</div>
        <div class="sim-bonus-note">&#10003; Bonus goles +3 incluido &nbsp;&middot;&nbsp; &#10007; Bonus clasificado no incluido</div>
      </div>
      <button class="sim-reset-btn" id="sim-reset-btn">&#8635; Reiniciar</button>
    </div>
    <div class="sim-body">
      <div class="sim-left" id="sim-matches"></div>
      <div class="sim-right">
        <div class="sim-right-header">Tabla proyectada</div>
        <div class="sim-rank-header">
          <span style="text-align:center">#</span><span>Jugador</span><span>Actual</span><span>+Sim</span><span>Total</span><span>&#916;</span>
        </div>
        <div id="sim-rank-list"></div>
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
      <div class="tool-subtitle">Estadisticas destacadas de la fase de grupos — calculadas automaticamente</div>
    </div>
    <div class="tool-body" id="badges-body"></div>
  </div>

  <div class="tool-content" id="matrix-content" style="display:none">
    <div class="tool-header">
      <div class="tool-title"><div class="section-bar" style="background:var(--cyan)"></div>Matriz de Predicciones</div>
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
  </div>

  <nav class="mobile-bnav">
    <button class="mob-btn active" data-target="section-chart"><span class="mi">&#128200;</span>Evol.</button>
    <button class="mob-btn" data-target="section-ranking"><span class="mi">&#127942;</span>Tabla</button>
    <button class="mob-btn" data-target="section-bracket"><span class="mi">&#9917;</span>Bracket</button>
    <button class="mob-btn" data-panel="sim"><span class="mi">&#127922;</span>Sim.</button>
    <button class="mob-btn" data-panel="relator"><span class="mi">&#127908;</span>Relator</button>
    <button class="mob-btn" data-panel="badges"><span class="mi">&#127941;</span>Premios</button>
    <button class="mob-btn" data-panel="matrix"><span class="mi">&#128202;</span>Preds.</button>
    <button class="mob-btn" data-panel="dificultad"><span class="mi">&#127919;</span>Dific.</button>
  </nav>

</div>

<script>
var _reAcc = new RegExp('[\\u0300-\\u036f]', 'g');
function abbrevTeam(t){var s=t.trim().normalize('NFD').replace(_reAcc,'').replace(/^(RI de |Rep\. de |Rep\. |RD |Estados |Arabia |Nueva )/i,'');return s.substring(0,3).toUpperCase();}
function abbrevMatch(name){var p=name.split(' vs ');return p.length===2?abbrevTeam(p[0])+'-'+abbrevTeam(p[1]):name.substring(0,7);}
function resultType(score){var p=score.split('-').map(Number);if(isNaN(p[0])||isNaN(p[1]))return'tie';return p[0]>p[1]?'local':p[0]<p[1]?'away':'tie';}
function formDotClass(pts){if(!pts)return'miss';if(pts>=7)return'bonus';if(pts>=5)return'exact';return'common';}
function _pick(arr){return arr[Math.floor(Math.random()*arr.length)];}

var _winProbs=null;
function calcWinProbs(data){
  var N=6000,players=data.players,base={};
  data.ranking.forEach(function(r){base[r.name]=r.pts;});
  var dists={};
  players.forEach(function(p){
    var h=data.history[p]||[0],d=[],tot;
    for(var i=1;i<h.length;i++)d.push(h[i]-h[i-1]);
    tot=d.length||1;
    var nm=0,nc=0,ne=0,nb=0;
    d.forEach(function(v){if(!v)nm++;else if(v<5)nc++;else if(v<9)ne++;else nb++;});
    dists[p]={m:nm/tot,c:nc/tot,e:ne/tot,b:nb/tot};
  });
  var rem=(data.knockout_matches||[]).filter(function(m){return!m.played;});
  var phE={'16avos':5,'Octavos':7,'Cuartos':10,'Semis':13,'3er Puesto':10,'Final':16};
  var phC={'16avos':2,'Octavos':3,'Cuartos':4,'Semis':5,'3er Puesto':4,'Final':6};
  if(!rem.length){
    var mxB=Math.max.apply(null,players.map(function(p){return base[p]||0;}));
    var pb={};players.forEach(function(p){pb[p]=(base[p]||0)===mxB?1:0;});return pb;
  }
  var wins={};players.forEach(function(p){wins[p]=0;});
  for(var s=0;s<N;s++){
    var sp={};players.forEach(function(p){sp[p]=base[p]||0;});
    rem.forEach(function(m){
      var ex=phE[m.phase]||5,cm=phC[m.phase]||2;
      players.forEach(function(p){
        var ds=dists[p],r=Math.random(),pts=0;
        if(r<ds.m)pts=0;
        else if(r<ds.m+ds.c)pts=cm;
        else if(r<ds.m+ds.c+ds.e)pts=ex;
        else pts=ex+2;
        if(Math.random()<0.5)pts+=2;
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
function renderBracket(data){_koData=data;var ko=data.knockout_matches;var br=document.getElementById('bracket'),svg=document.getElementById('bracket-svg');var phOrd=['16avos','Octavos','Cuartos','Semis','Final','3er Puesto'],phMap={};ko.forEach(function(m){if(!phMap[m.phase])phMap[m.phase]=[];phMap[m.phase].push(m);});var html='';phOrd.forEach(function(phase){var ms=phMap[phase];if(!ms||!ms.length)return;var meta=PHASE_META[phase]||{label:phase.toUpperCase(),color:'#00e5ff'};var slots=ms.map(function(m){var cls='bm';if(m.is_tbd)cls+=' tbd';else if(!m.show_preds)cls+=' locked';else if(m.has_preds)cls+=' clickable';if(m.played)cls+=' played';if(phase==='Final')cls+=' bm-final';if(phase==='3er Puesto')cls+=' bm-3rd';var mnCls=m.is_tbd?'bm-match tbd-name':'bm-match';var dots='';if(!m.is_tbd&&m.show_preds&&data.players){var cnt=data.players.filter(function(p){return!!m.predictions[p];}).length;dots='<div class="bm-dots">';for(var d=0;d<Math.min(cnt,8);d++)dots+='<div class="bd on'+(m.played?' played':'')+'"></div>';for(var d2=cnt;d2<8;d2++)dots+='<div class="bd"></div>';dots+='</div>';}else if(!m.is_tbd&&!m.show_preds){dots='<div class="bm-lock">&#128274;'+(m.match_date?' '+m.match_date:'')+'</div>';}return'<div class="'+cls+'" data-id="'+m.id+'"><div class="bm-id">'+m.id+'</div><div class="'+mnCls+'">'+m.match+'</div>'+dots+'</div>';}).join('');html+='<div class="br-col" data-phase="'+phase+'"><div class="br-col-header" style="color:'+meta.color+'">'+meta.label+'</div><div class="br-slots">'+slots+'</div></div>';});br.innerHTML=html;br.appendChild(svg);br.querySelectorAll('.bm.clickable').forEach(function(card){card.addEventListener('click',function(){var mid=this.dataset.id;var match=ko.find(function(m){return m.id===mid;});if(!match)return;var was=this.classList.contains('selected');br.querySelectorAll('.bm').forEach(function(c){c.classList.remove('selected');});if(was){closePredDetail();return;}this.classList.add('selected');showPredDetail(match);});});requestAnimationFrame(function(){requestAnimationFrame(drawBracketLines);});}

var PHASE_PTS={'16avos':{common:2,exact:5},'Octavos':{common:3,exact:7},'Cuartos':{common:3,exact:7},'Semis':{common:3,exact:7},'3er Puesto':{common:3,exact:7},'Final':{common:5,exact:10}};
var _DEMO_NAMES={'P73':'Uruguay vs Mexico','P74':'Argentina vs Ecuador','P75':'Brasil vs Venezuela','P76':'Colombia vs Peru','P77':'USA vs Panama','P78':'Canada vs El Salvador','P79':'Francia vs Marruecos','P80':'Espana vs Suiza','P81':'Alemania vs Escocia','P82':'Portugal vs Turquia','P83':'Inglaterra vs Rep. Checa','P84':'Holanda vs Dinamarca','P85':'Japon vs Australia','P86':'Korea Sur vs Senegal','P87':'Italia vs Polonia','P88':'Croacia vs Rumania'};
var _DPATS=[['2-0','2-1','1-0','2-0','2-1','1-0','1-1','0-1','2-1','2-0','1-0','0-1','1-1','2-0','1-0','0-1'],['1-0','0-1','1-1','2-1','0-2','1-0','2-0','1-2','1-1','0-1','2-1','1-0','0-2','1-1','2-0','0-1'],['0-1','0-2','1-2','0-1','1-1','0-2','2-1','0-1','1-0','0-2','1-1','0-1','2-0','0-1','1-2','0-1'],['1-1','2-2','0-0','1-1','2-1','0-1','1-1','2-0','0-0','1-2','1-1','0-1','2-1','1-1','0-2','1-1'],['2-1','1-2','2-0','1-1','0-1','2-1','1-0','0-2','1-1','2-1','0-1','1-0','2-0','1-1','0-1','2-1'],['1-0','2-0','0-1','1-0','2-1','1-0','0-1','1-1','1-0','2-0','0-1','2-1','1-0','0-2','1-1','1-0']];
var _simData=null,_simMatches=[];
function _buildSimMatches(data){return data.knockout_matches.map(function(m,idx){if(!m.has_preds||m.is_tbd){var pat=_DPATS[idx%_DPATS.length];var off=idx%16;var rot=pat.slice(off).concat(pat.slice(0,off));var preds={};data.players.forEach(function(p,i){preds[p]=rot[i%rot.length];});return Object.assign({},m,{match:m.match||_DEMO_NAMES[m.id],is_tbd:false,has_preds:true,predictions:preds});}return m;});}
function _sign(l,a){return l>a?1:l<a?-1:0;}
function _calcPts(pred,score,phase){if(!pred||!score)return 0;var pts=PHASE_PTS[phase]||{common:3,exact:7};var pp=pred.split('-').map(Number);if(isNaN(pp[0])||isNaN(pp[1]))return 0;if(_sign(pp[0],pp[1])!==_sign(score.l,score.a))return 0;var exact=(pp[0]===score.l&&pp[1]===score.a);var base=exact?pts.exact:pts.common;if(exact){var predDiff=Math.abs(pp[0]-pp[1]),actualDiff=Math.abs(score.l-score.a);if(predDiff>=3&&actualDiff>=3)base+=2;}return base;}
function _getScores(){var sc={};document.querySelectorAll('.sim-card').forEach(function(card){var id=card.dataset.simId;var inps=card.querySelectorAll('.sim-inp');var lv=inps[0]?inps[0].value.trim():'',av=inps[1]?inps[1].value.trim():'';if(lv!==''&&av!==''&&!isNaN(+lv)&&!isNaN(+av)){sc[id]={l:+lv,a:+av};card.classList.add('has-score');}else{card.classList.remove('has-score');}});return sc;}
function _updateSimRanking(){if(!_simData)return;var scores=_getScores();var simPts={};_simData.players.forEach(function(p){simPts[p]=0;});_simMatches.forEach(function(m){var sc=scores[m.id],clsSide=_simClassif[m.id];if(!sc&&!clsSide)return;_simData.players.forEach(function(p){if(sc)simPts[p]+=_calcPts(m.predictions[p],sc,m.phase);if(clsSide&&m.classif&&m.classif[p])simPts[p]+=_classifBonus(m.classif[p],m.match,clsSide);});});var proj=_simData.ranking.map(function(r){return{name:r.name,cur:r.pts,sim:simPts[r.name]||0,curPos:r.pos,total:r.pts+(simPts[r.name]||0)};});proj.sort(function(a,b){return b.total-a.total||(a.name>b.name?1:-1);});var pc3=['p1','p2','p3'];document.getElementById('sim-rank-list').innerHTML=proj.map(function(r,i){var pp=i+1,pc=pp<=3?pc3[pp-1]:'';var delta=r.curPos-pp;var dH=delta>0?'<span style="color:var(--green)">&#9650;'+delta+'</span>':delta<0?'<span style="color:var(--pink)">&#9660;'+Math.abs(delta)+'</span>':'<span style="color:var(--muted)">&mdash;</span>';var sH=r.sim>0?'<span style="color:var(--green)">+'+r.sim+'</span>':'<span style="color:var(--muted)">+0</span>';var c=_simData.colors[r.name]||'#888';return'<div class="sim-rank-row"><div class="sim-rank-pos '+pc+'">'+pp+'</div><div class="sim-rank-name"><span class="clr-dot" style="background:'+c+'"></span>'+r.name+'</div><div class="sim-rank-num">'+r.cur+'</div><div class="sim-rank-num">'+sH+'</div><div class="sim-rank-total '+pc+'">'+r.total+'</div><div class="sim-rank-delta">'+dH+'</div></div>';}).join('');}
function renderSim(data){_simData=data;_simClassif={};_simMatches=_buildSimMatches(data);var phOrd=['16avos','Octavos','Cuartos','Semis','Final','3er Puesto'],phMap={};_simMatches.forEach(function(m){if(!phMap[m.phase])phMap[m.phase]=[];phMap[m.phase].push(m);});var html='';phOrd.forEach(function(phase){var ms=phMap[phase];if(!ms||!ms.length)return;var meta=PHASE_META[phase]||{label:phase.toUpperCase(),color:'#00e5ff'};var pts=PHASE_PTS[phase]||{common:3,exact:7};html+='<div class="sim-phase-lbl" style="color:'+meta.color+'">'+meta.label+'<span class="sim-phase-pts">com. '+pts.common+'pts &middot; exacto '+pts.exact+'pts &middot; cls. +2pts</span></div>';ms.forEach(function(m){var predCnt=data.players.filter(function(p){return!!m.predictions[p];}).length;var clsCnt=m.classif?Object.keys(m.classif).length:0;var teams=m.match.split(' v '),localT=teams[0]||'Local',visitT=teams.length>1?teams[1]:'Visitante';var clsRow=clsCnt>0?'<div class="sim-cls-row"><span class="sim-cls-lbl">Pasa:</span><button class="sim-cls-btn" data-cls-id="'+m.id+'" data-side="L">'+localT+'</button><button class="sim-cls-btn" data-cls-id="'+m.id+'" data-side="V">'+visitT+'</button></div>':'';html+='<div class="sim-card" data-sim-id="'+m.id+'"><div class="sim-card-top"><div class="sim-card-name">'+m.match+'</div><div class="sim-card-id">'+m.id+'</div></div><div class="sim-score-row"><input type="number" min="0" max="20" class="sim-inp" placeholder="?"><span class="sim-sep">&#8722;</span><input type="number" min="0" max="20" class="sim-inp" placeholder="?"><span class="sim-ok">&#10003; ok</span></div>'+clsRow+'<div class="sim-pred-cnt">'+predCnt+'/'+data.players.length+' preds'+(clsCnt>0?' &middot; '+clsCnt+' cls.':'')+'</div></div>';});});document.getElementById('sim-matches').innerHTML=html;document.querySelectorAll('.sim-inp').forEach(function(inp){inp.addEventListener('input',_updateSimRanking);});document.querySelectorAll('.sim-cls-btn').forEach(function(btn){btn.addEventListener('click',function(){var id=this.dataset.clsId,side=this.dataset.side;if(_simClassif[id]===side){delete _simClassif[id];document.querySelectorAll('.sim-cls-btn[data-cls-id="'+id+'"]').forEach(function(b){b.classList.remove('active');});}else{_simClassif[id]=side;document.querySelectorAll('.sim-cls-btn[data-cls-id="'+id+'"]').forEach(function(b){b.classList.toggle('active',b.dataset.side===side);});}  _updateSimRanking();});});document.getElementById('sim-reset-btn').onclick=function(){document.querySelectorAll('.sim-inp').forEach(function(inp){inp.value='';});document.querySelectorAll('.sim-card').forEach(function(c){c.classList.remove('has-score');});document.querySelectorAll('.sim-cls-btn').forEach(function(b){b.classList.remove('active');});_simClassif={};_updateSimRanking();};_updateSimRanking();}

var _simClassif={};
function _normalizeTeam(s){return s.trim().toLowerCase().normalize('NFD').replace(_reAcc,'');}
function _classifBonus(playerPred,matchName,actualSide){
  if(!playerPred)return 0;
  var parts=matchName.split(' v ');
  if(parts.length<2)return 0;
  var actualTeam=actualSide==='L'?parts[0].trim():parts[1].trim();
  return _normalizeTeam(playerPred)===_normalizeTeam(actualTeam)?2:0;
}

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
  var rk=data.ranking, n=rk.length;
  var ldr=rk[0],sec=rk[1],trd=rk[2],lst=rk[n-1],slst=rk[n-2];
  var g12=ldr.pts-sec.pts, g23=sec.pts-trd.pts, gBot=ldr.pts-lst.pts;
  var played=data.group_total||data.matches_played.length;
  var koStarted=data.knockout_matches&&data.knockout_matches.some(function(m){return m.played;});
  var koPhase=koStarted?'Fase eliminatoria en curso.':'Primera jornada eliminatoria arrancando hoy.';

  var formD=rk.map(function(r){
    var hist=data.history[r.name]||[0],d=[];
    for(var i=1;i<hist.length;i++)d.push(hist[i]-hist[i-1]);
    var tot=d.length||1;
    return{
      name:r.name,pos:r.pos,pts:r.pts,
      last5:d.slice(-5).reduce(function(a,b){return a+b;},0),
      exactos:d.filter(function(x){return x>=5;}).length,
      exactosB:d.filter(function(x){return x===7;}).length,
      avg:Math.round(r.pts/tot*10)/10,
      total:d.length
    };
  });
  var sorted_avg=formD.slice().sort(function(a,b){return b.avg-a.avg;});
  var bf=formD.slice().sort(function(a,b){return b.last5-a.last5;})[0];
  var mx=formD.slice().sort(function(a,b){return(b.exactos+b.exactosB)-(a.exactos+a.exactosB);})[0];
  var mxTot=mx?(mx.exactos+mx.exactosB):0;

  var lines=[];

  // Apertura: contexto del torneo, sin euforia
  lines.push(_pick([
    'Fase de grupos cerrada: '+played+'/72 partidos registrados en el sistema. '+koPhase+' Este es el primer Mundial con formato de 48 selecciones — la fase de grupos genero el doble de partidos que en 2018.',
    played+' partidos de grupos procesados (72 en total). '+koPhase+' A partir de aca los puntos no son lineales: un exacto en 16avos vale 5, en cuartos escala, y en la final llega a 10.',
    'Grupos completados. '+koPhase+' El prode entra en la etapa donde la estructura de puntos cambia: cada fase multiplica el valor de los aciertos, y el clasificado agrega +2 independientemente del resultado.',
  ]));

  // Liderazgo: análisis frío
  var ldrFd=formD.find(function(f){return f.name===ldr.name;});
  if(g12===0){
    lines.push(ldr.name+' y '+sec.name+' igualados en la cima con '+ldr.pts+' pts. Empate exacto después de '+played+' partidos. El primer partido eliminatorio los va a separar — o no.');
  } else if(g12===1){
    lines.push(ldr.name+' encabeza con '+ldr.pts+' pts, un punto arriba de '+sec.name+'. Diferencia mínima: cualquier exacto en el eliminatorio la borra. El margen actual equivale a menos de la mitad de un resultado común (2 pts).');
  } else if(g12<=5){
    lines.push(ldr.name+' lidera con '+ldr.pts+' pts. Ventaja de '+g12+' sobre '+sec.name+' ('+sec.pts+'). En términos del eliminatorio, eso es entre uno y dos resultados comunes — aun insuficiente para considerarse seguro.');
  } else {
    lines.push(ldr.name+' cierra la fase de grupos en el primer puesto con '+ldr.pts+' pts y '+g12+' de ventaja sobre '+sec.name+'. Promedio de '+ldrFd.avg+' pts por partido en grupos — el '+(sorted_avg[0].name===ldr.name?'mayor':'uno de los mayores')+' del prode. La ventaja es real pero no definitiva.');
  }

  // Podio
  var g23str=g23===0?'igualados':(g23+' pt'+(g23!==1?'s':''));
  lines.push('Podio provisional: '+ldr.name+' ('+ldr.pts+'), '+sec.name+' ('+sec.pts+'), '+trd.name+' ('+trd.pts+'). Entre 2do y 3ro: '+g23str+'. Con 16 partidos de 16avos más las fases siguientes, ningún lugar del podio está consolidado.');

  // Forma reciente
  if(bf&&bf.last5>0){
    lines.push(_pick([
      bf.name+' tuvo el mejor cierre de grupos: '+bf.last5+' pts en los últimos 5 partidos. Ese rendimiento final puede indicar que calibró bien los equipos hacia el final — dato relevante de cara al eliminatorio.',
      'Últimos 5 partidos del grupo: '+bf.name+' lidera con '+bf.last5+' pts. La tendencia al alza al final de la fase puede tener continuidad en 16avos si los equipos que pronosticó avanzaron.',
    ]));
  }

  // Exactos — métrica de calidad
  if(mxTot>0){
    lines.push(_pick([
      'Métrica de precisión: '+mx.name+' acumula '+mxTot+' exactos en grupos ('+mx.exactos+' simples, '+mx.exactosB+' con bonus de diferencia). Clavar un marcador exacto requiere acierto en ganador, goles locales y goles visitantes simultáneamente — la tasa de exactos es el mejor indicador de calidad predictiva.',
      mx.name+' lidera en exactos con '+mxTot+' en la fase de grupos. En un Mundial con 72 partidos, la probabilidad de acertar un marcador exacto al azar ronda el 3-5% por partido. '+mxTot+' exactos en '+played+' partidos supera ampliamente esa línea base.',
    ]));
  }

  // Fondo de tabla: análisis de remontada
  lines.push(_pick([
    lst.name+' cierra la tabla con '+lst.pts+' pts, a '+gBot+' del líder. Para llegar al podio necesita una combinación específica: que los de arriba fallen en el eliminatorio mientras él acierta. No imposible, pero requiere divergencia simultánea en múltiples partidos.',
    'El puesto '+n+' lo tiene '+lst.name+' con '+lst.pts+' pts. La brecha con el líder es '+gBot+'. El potencial máximo teórico del eliminatorio (si se acierta todo con clasificados) puede mover la tabla en +80 pts o más — la matemática del formato favorece las remontadas, aunque en la práctica la consistencia se mantiene.',
  ]));

  // Cierre contextual
  lines.push(_pick([
    'El formato de puntos escala por fase: 16avos (2/5+2cls), octavos (3/7+2cls), cuartos (4/10+2cls), semis y final con valores aún mayores. La primera fecha eliminatoria ya está en juego. Actualizar después de cada jornada.',
    'Los $400.000 siguen abiertos. La ventaja acumulada en grupos pesa, pero el eliminatorio tiene suficiente volumen de puntos como para reconfigurar la tabla. Próxima lectura relevante: después de los 16avos.',
    'Con '+n+' jugadores, la dispersión de puntajes sugiere que la competencia es ajustada. El eliminatorio va a amplificar las diferencias de quienes pronosticaron bien los clasificados — esa es la variable nueva e impredecible de esta edición.',
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
function renderRelator(data){_relatorData=data;document.getElementById('relator-btn').onclick=_relateNow;}

function renderBadges(data){
  var players=data.players,colors=data.colors,N=players.length;
  var gp=data.group_preds||[];
  // Compute per-player stats
  var st={};
  players.forEach(function(p){
    var hist=data.history[p]||[0],d=[];
    for(var i=1;i<hist.length;i++)d.push(hist[i]-hist[i-1]);
    var n=d.length||1, pts=data.ranking.find(function(r){return r.name===p;}).pts;
    var mean=pts/n;
    var variance=d.reduce(function(s,x){return s+(x-mean)*(x-mean);},0)/n;
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
  var html='<div class="badges-grid">';
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
  document.getElementById('badges-body').innerHTML=html;
}

function renderMatrix(data){
  var players=data.players,colors=data.colors,gp=data.group_preds||[];
  if(!gp.length){document.getElementById('matrix-body').innerHTML='<p style="color:var(--muted);padding:20px">Sin datos de predicciones de grupos.</p>';return;}
  var abbr=function(n){return n.split(' ')[0].substring(0,7);};
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
  gp.forEach(function(m){
    var N=players.length;
    var ac=players.filter(function(p){return(m.pts[p]||0)>0;}).length;
    var diffCls=ac<=Math.floor(N*0.3)?'diff-hard':ac<=Math.floor(N*0.5)?'diff-med':'';
    var actualRes=null;
    players.forEach(function(p){if(!actualRes&&(m.pts[p]||0)>=5&&m.predictions[p])actualRes=m.predictions[p];});
    html+='<tr class="'+diffCls+'">';
    html+='<td class="matrix-match-name" title="'+m.match+'">'+m.match.replace(/ vs /g,' v ').substring(0,22)+(m.match.length>22?'&#8230;':'')+'</td>';
    html+='<td class="matrix-actual">'+(actualRes||'?')+'</td>';
    players.forEach(function(p){
      var pred=m.predictions[p],pts=m.pts[p]||0;
      var cls=pts>=5?'mx-exact':pts>=2?'mx-common':'mx-miss';
      html+='<td class="matrix-cell '+cls+'" title="'+p+': '+(pred||'—')+' ('+pts+'pts)">'+(pred||'—')+'</td>';
    });
    html+='</tr>';
  });
  html+='</tbody></table></div>';
  document.getElementById('matrix-body').innerHTML=html;
}

function renderDifficulty(data){
  var players=data.players,gp=data.group_preds||[],N=players.length;
  if(!gp.length){document.getElementById('dificultad-body').innerHTML='<p style="color:var(--muted);padding:20px">Sin datos.</p>';return;}
  var matches=gp.map(function(m){
    var ac=players.filter(function(p){return(m.pts[p]||0)>0;}).length;
    var ex=players.filter(function(p){return(m.pts[p]||0)>=5;}).length;
    var actualRes=null;
    players.forEach(function(p){if(!actualRes&&(m.pts[p]||0)>=5&&m.predictions[p])actualRes=m.predictions[p];});
    return{id:m.id,match:m.match,ac:ac,ex:ex,pct:ac/N,actualRes:actualRes};
  }).sort(function(a,b){return a.ac-b.ac;});
  var html='<table class="dif-table"><thead><tr>';
  html+='<th>#</th><th>Partido</th><th>Resultado</th><th>Acertaron</th><th>Exactos</th><th>Dificultad</th>';
  html+='</tr></thead><tbody>';
  matches.forEach(function(m,i){
    var barW=Math.round((1-m.pct)*100);
    var label=m.pct<=0.25?'&#128308; Muy dificil':m.pct<=0.5?'&#128992; Dificil':m.pct<=0.75?'&#128993; Moderado':'&#128994; Facil';
    html+='<tr>';
    html+='<td><span class="dif-rank-badge">'+(i+1)+'</span></td>';
    html+='<td class="dif-match">'+m.match+'</td>';
    html+='<td class="dif-result">'+(m.actualRes||'—')+'</td>';
    html+='<td class="dif-num">'+m.ac+'/'+N+'</td>';
    html+='<td class="dif-num">'+m.ex+'</td>';
    html+='<td class="dif-bar-cell"><div class="dif-bar"><div class="dif-fill" style="width:'+barW+'%"></div></div><span class="dif-label">'+label+'</span></td>';
    html+='</tr>';
  });
  html+='</tbody></table>';
  document.getElementById('dificultad-body').innerHTML=html;
}

function initNav(){
  var mc=document.getElementById('main-content');
  var panels={sim:document.getElementById('sim-content'),relator:document.getElementById('relator-content'),badges:document.getElementById('badges-content'),matrix:document.getElementById('matrix-content'),dificultad:document.getElementById('dificultad-content')};
  var navItems=document.querySelectorAll('.nav-item');
  var sections=['section-chart','section-ranking','section-bracket'];
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
    renderSim(data);
    renderRelator(data);
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
