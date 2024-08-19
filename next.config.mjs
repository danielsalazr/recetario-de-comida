/** @type {import('next').NextConfig} */
const nextConfig = {
  // reactStrictMode: true,
  
  output: 'export',
  trailingSlash: true,
  skipTrailingSlashRedirect: true,
  distDir: 'dist',
  // cacheHandler: require.resolve('./cache-handler.js'),
  // cacheMaxMemorySize: 0, // disable default in-memory caching
};

export default nextConfig;
