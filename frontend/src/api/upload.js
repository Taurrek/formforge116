export const uploadBundle = async (file) => {
  // Stub: bypass real S3, just point to the local ZIP
  return { url: '/investor_bundle.zip' };
};
