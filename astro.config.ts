// @ts-check
import starlight from "@astrojs/starlight";
import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://docs.animexx.org",
  // Listen on all interfaces so the dev server is reachable from outside the dev container
  // server: { host: true },
  integrations: [
    starlight({
      title: "Animexx e. V.",
      description: "Dokumentensammlung des Animexx e. V.",
      prerender: true,
      defaultLocale: "root",
      locales: {
        root: { label: "Deutsch", lang: "de" },
      },
      favicon: "/favicon.ico",
      logo: {
        light: "./src/assets/logo-light.svg",
        dark: "./src/assets/logo-dark.svg",
        replacesTitle: true,
      },
      lastUpdated: true,
      editLink: {
        baseUrl: "https://github.com/Animexx/docs/edit/main/",
      },
      customCss: [
        "@fontsource-variable/source-sans-3/index.css",
        "@fontsource-variable/source-code-pro/index.css",
        "./src/styles/custom.css",
      ],
      components: {
        Footer: "./src/components/Footer.astro",
      },
      sidebar: [
        "index",
        "erscheinungsbild",
        {
          label: "Satzung & Ordnungen",
          items: [{ autogenerate: { directory: "governance" } }],
        },
      ],
    }),
  ],
  // Previous URLs before the folder structure was introduced
  redirects: {
    "/satzung": "/governance/satzung/",
    "/gov_verein": "/governance/gov_verein/",
    "/gov_aktivenrat": "/governance/gov_aktivenrat/",
  },
});
