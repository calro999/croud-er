"use client";

import { useEffect, useRef } from "react";

interface FanzaBannerProps {
  bannerId?: string;
  affiliateId?: string;
  width?: number;
  height?: number;
}

export default function FanzaBanner({
  bannerId = "164_300_250",
  affiliateId = "onchan555-003",
  width = 300,
  height = 250,
}: FanzaBannerProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    containerRef.current.innerHTML = "";

    const iframe = document.createElement("iframe");
    iframe.style.width = `${width}px`;
    iframe.style.height = `${height}px`;
    iframe.style.border = "none";
    iframe.style.overflow = "hidden";
    iframe.scrolling = "no";

    containerRef.current.appendChild(iframe);

    const doc = iframe.contentDocument || iframe.contentWindow?.document;
    if (doc) {
      doc.open();
      doc.write(`
        <!DOCTYPE html>
        <html>
        <head>
          <style>
            html, body {
              margin: 0;
              padding: 0;
              overflow: hidden;
              background: transparent;
              width: ${width}px;
              height: ${height}px;
              display: flex;
              justify-content: center;
              align-items: center;
            }
            a.fallback-banner {
              display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: center;
              width: 100%;
              height: 100%;
              background: linear-gradient(135deg, #1e1b4b, #881337);
              color: #fff;
              text-decoration: none;
              border-radius: 12px;
              border: 1px solid #fda4af;
              font-family: sans-serif;
              text-align: center;
              padding: 12px;
              box-sizing: border-box;
            }
            a.fallback-banner:hover {
              filter: brightness(1.1);
            }
          </style>
        </head>
        <body>
          <ins class="widget-banner"></ins>
          <script class="widget-banner-script" src="https://widget-view.dmm.co.jp/js/banner_placement.js?affiliate_id=${affiliateId}&banner_id=${bannerId}"></script>
          <script>
            setTimeout(function() {
              var ins = document.querySelector('.widget-banner');
              if (ins && (!ins.children || ins.children.length === 0)) {
                ins.innerHTML = '<a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F&af_id=${affiliateId}" target="_blank" class="fallback-banner"><span style="font-size:26px;margin-bottom:6px;">🎬</span><strong style="font-size:15px;color:#fff;">FANZA 見放題ch 公式ページ</strong><span style="font-size:12px;color:#fecdd3;margin-top:6px;font-weight:bold;">圧倒的作品数！見放題を体験する ›</span></a>';
              }
            }, 1500);
          </script>
        </body>
        </html>
      `);
      doc.close();
    }
  }, [bannerId, affiliateId, width, height]);

  return (
    <div
      ref={containerRef}
      style={{
        width: `${width}px`,
        height: `${height}px`,
        display: "inline-flex",
        justifyContent: "center",
        alignItems: "center",
        overflow: "hidden",
      }}
    />
  );
}
