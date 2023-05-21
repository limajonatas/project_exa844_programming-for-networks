import { api } from "../boot/axios";

export default {
  async getByGender() {
    const response = await api.get();
    return response.data.by_gender;
  },
};
